from pydantic import BaseModel, EmailStr, Field

class ProveedorCreate(BaseModel):
    nombre: str = Field(..., max_length=50)
    direccion: str = Field(..., max_length=50)
    telefono: str = Field(..., max_length=50)
    email: EmailStr