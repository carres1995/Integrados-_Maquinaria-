from pydantic import BaseModel
from uuid import UUID
from datetime import date

class MaquinariRespose(BaseModel):
    id : UUID
    nombre : str 
    tipo : str
    modelo : str 
    serie : str 
    ubicacion : str 
    fecha_adquisicion: date
    estado : str 
    
    class Config:
        from_attributes = True