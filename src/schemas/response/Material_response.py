from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal

class MaterialResponse(BaseModel):
    id: UUID
    nombre_material: str
    tipo: str
    unidad_medida: str
    vida_util: Decimal
    stock_minimo: Decimal
    stock_actual: Decimal
    stock_maximo: Decimal
    proveedor_id: UUID 

    class Config:
        from_attributes = True