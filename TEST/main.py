from fastapi import Depends, FastAPI, Form
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Biker
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
def create_biker(db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):

    # db.add(db_biker)
    # db.commit()
    # db.refresh(db_biker)
    biker_model = models.Biker()
    biker_model.username = username
    biker_model.password = password

    db.add(biker_model)
    db.commit()

    return {"message": "Biker created successfully", "biker" : biker_model}

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Biker).all()