from pydantic import BaseModel, Field
from datetime import date



class MaquinariaCreate(BaseModel):
    nombre : str = Field(..., max_length=50)
    tipo : str = Field(..., max_length=50)
    modelo : str = Field(..., max_length=50)
    serie : str = Field(..., max_length=50)
    ubicacion : str = Field(..., max_length=50)
    fecha_adquisicion: date
    estado : str = Field(..., max_length=50)
    
    
    