from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

class Post(BaseModel):
    title : str
    description : str


app = FastAPI()


try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
    password='collins2005', cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    print("db success")
except Exception as e:
    print(e)

    
@app.get("/theposts")
def get_posts():
    cursor.execute(""" SELECT * from posts """)
    posts = cursor.fetchall()
    print(posts)
    return {'data' : posts}

@app.get("/posts")
def create_post():
    posts = cursor.execute(""" SELECT * from posts """)
    print(posts)
    return {'data' : posts}


