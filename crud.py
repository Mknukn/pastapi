from sqlalchemy.orm import Session
import models, schemas

def get_pasta(db: Session, pasta_id: int):
    return db.query(models.Pasta).filter(models.Pasta.id == pasta_id).first()

def get_pastas(db: Session, skip: int=0, limit: int = 10):
    return db.query(models.Pasta).offset(skip).limit(limit).all()

def create_pasta(db: Session, item: schemas.PastaCreate):
    db_item = models.Pasta(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item