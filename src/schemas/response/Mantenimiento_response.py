from pydantic import BaseModel
from uuid import UUID
from datetime import date

class MantenimientoResponse(BaseModel):
    id: UUID
    maquinaria_id: UUID
    tipo_mantenimiento: str
    fecha_inicio: date
    fecha_fin: date
    descripcion: str
    responsable: str
    estado: str

    class Config:
        from_attributes = True