from fastapi import Depends, FastAPI, Form, Request
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Biker
from typing import Union
from . import models
from .schemas import Biker as BikerSchema

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Dependency to provide a database session to each request


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bikers/")
async def create_biker(request: Request, db: Session = Depends(get_db)):
    content_type = request.headers.get("content-type")

    if "multipart/form-data" in content_type:
        biker = BikerSchema(
            username=str(Form(...)),
            password=str(Form(...))
        )
    else:  # Assuming JSON request
        biker = BikerSchema(**await request.json())

    # db.add(db_biker)r9
    # db.commit()
    # db.refresh(db_biker)
    biker_model = Biker()
    biker_model.username = biker.username
    biker_model.password = biker.password

    db.add(biker_model)
    db.commit()

    return {"message": "Biker created successfully", "biker": biker_model}


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Biker).all()
