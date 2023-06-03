from fastapi import FastAPI
app = FastAPI()

db: List[User] = [

]

@app.get("/")
def root() : 
    return { "Hello" : "World" }
 