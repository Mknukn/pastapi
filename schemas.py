from pydantic import BaseModel

class PastaBase(BaseModel):
    name: str
    description: str | None = None

class PastaCreate(PastaBase):
    pass 

class Pasta(PastaBase):
    id: int
    
    class Config:
        orm_mode = True
