from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class MantenimientosCreate(BaseModel):
    id:UUID
    maquinaria_id: UUID
    tipo_mantenimiento: str = Field(..., max_length=50)
    fecha_inicio: datetime
    fecha_fin: datetime
    descripcion : str  
    responsable : str = Field(..., max_length= 50)
    estado: str = Field(..., max_length= 50)
    