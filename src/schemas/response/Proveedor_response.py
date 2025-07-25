from uuid import UUID
from pydantic import BaseModel, EmailStr

class ProveedorResponse(BaseModel):
    id: UUID
    nombre: str
    direccion: str
    telefono: str
    email: EmailStr

    class Config:
        from_attributes = True  
