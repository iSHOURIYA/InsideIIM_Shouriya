from app.core.config import get_settings


def get_secret_key() -> str:
    return get_settings().secret_key
