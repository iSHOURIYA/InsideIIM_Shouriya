from fastapi import FastAPI

app = FastAPI()
@app.get("/login") 
def Health(username : str | None = None, password : str | None = None) -> str:
    if (username == "mine" and password == "1234") :
        return "Login Success !"   
    return "Hey I am UP , so send ID and Pass for entry" ;

def sayHello(fName : str , lName : str) -> str:
    return fName + " " + lName
    
    
abc = sayHello("Shouriya" , "Tayal") 
print(abc)