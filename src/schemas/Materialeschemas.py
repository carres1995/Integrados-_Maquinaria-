from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal

class MaterialCreate(BaseModel):
    nombre_material: str = Field(..., max_length=50)
    tipo: str = Field(..., max_length=50)
    unidad_medida: str = Field(..., max_length=50)
    vida_util: Decimal
    stock_minimo: Decimal
    stock_actual: Decimal
    stock_maximo: Decimal
    proveedor_id: UUID