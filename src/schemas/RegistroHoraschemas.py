from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date

class RegistroHorasCreate(BaseModel):
    maquinaria_id: UUID
    fecha: date
    horas_maquina: float
    actividad: str = Field(..., max_length=50)
    operador: str = Field(..., max_length=50)
