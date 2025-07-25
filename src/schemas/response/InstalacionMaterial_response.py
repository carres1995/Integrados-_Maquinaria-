from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date

class InstalacionMaterialResponse(BaseModel):
    id: UUID
    materiales_id: UUID
    maquinaria_id: UUID
    cantidad: float
    fecha_instalacion: date
    horas_maquina: float
    responsable: str = Field(..., max_length=50)
    estado: str = Field(..., max_length=50)

    class Config:
        from_attributes = True
