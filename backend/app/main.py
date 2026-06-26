from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_logging()
    yield


def register_router(app: FastAPI, prefix: str) -> None:
    for route in api_router.routes:
        if not isinstance(route, APIRoute):
            continue

        app.add_api_route(
            path=f"{prefix}{route.path}",
            endpoint=route.endpoint,
            methods=list(route.methods or []),
            name=route.name,
            response_model=route.response_model,
            status_code=route.status_code,
            tags=route.tags,
            summary=route.summary,
            description=route.description,
        )


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_router(app, settings.api_v1_prefix)
    return app


app = create_app()
