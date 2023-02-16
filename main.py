from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/pasta/{pasta_id}", response_model=schemas.Pasta)
def read_item(pasta_id: int, db: Session = Depends(get_db)):
    db_pasta = crud.get_pasta(db, pasta_id=pasta_id)
    if db_pasta:
        return db_pasta
    elif db_pasta is None:
        raise HTTPException(status_code=404, detail="Pasta not found")

@app.post("/api/pasta/add_pasta", response_model=schemas.Pasta)
def create_pasta(item: schemas.PastaCreate, db: Session = Depends(get_db)):
    print(item)
    return crud.create_pasta(db=db, item=item)