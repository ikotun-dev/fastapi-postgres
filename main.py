from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

class Post(BaseModel):
    title : str
 #   description : str


app = FastAPI()


try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
    password='collins2005', cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    print("db success")
except Exception as e:
    print(e)

    
@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * from posts """)
    posts = cursor.fetchall()
    print(posts)
    return {'data' : posts}

@app.post("/posts")
def create_post(post: Post):
    cursor.execute(""" INSERT INTO posts (title) VALUES (%s) RETURNING *""", (post.title,))
    new_post = cursor.fetchone()

    conn.commit()

    return {'data' : new_post}

@app.get("/posts/{id}")
def get_posts(id: str):
    cursor.execute(""" SELECT * from posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    return {'data' : post}


@app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id  = %s RETURNING * """, (str(id),))
    deleted_post =  cursor.fetchone()
    if deleted_post == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")  
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s  WHERE id = %s RETURNING *""",  (post.title, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {'data' : updated_post}

