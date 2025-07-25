from sqlalchemy.orm import Session
from src.models.Materiales import Materiales
from src.schemas.Materialeschemas import MaterialCreate
from uuid import UUID

def get_materiales(db:Session):
    return db.query(Materiales).all()

def get_material_id(db:Session, material_id: UUID):
    return db.query(Materiales).filter(Materiales.id == material_id).first()

def get_material_by_name(db:Session, nombre: str):
    return db.query(Materiales).filter(Materiales.nombre_material == nombre).first()

def create_material(db:Session, material:MaterialCreate):
    db_material = Materiales(
        nombre_material=material.nombre_material,
        tipo=material.tipo,
        unidad_medida=material.unidad_medida,
        vida_util=material.vida_util,
        stock_minimo=material.stock_minimo,
        stock_actual =material.stock_actual,
        stock_maximo=material.stock_maximo,
        proveedor_id=material.proveedor_id
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material_id:UUID, material_data: MaterialCreate):
    db_material = get_material_id(db, material_id)
    if db_material:
        db_material.nombre_material = material_data.nombre_material #type: ignore
        db_material.tipo = material_data.tipo #type: ignore
        db_material.unidad_medida = material_data.unidad_medida #type: ignore
        db_material.vida_util = material_data.vida_util #type: ignore
        db_material.stock_minimo = material_data.stock_minimo #type: ignore
        db_material.stock_actual = material_data.stock_actual #type: ignore
        db_material.stock_maximo = material_data.stock_maximo #type: ignore
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, material_id):
    db_material = get_material_id(db, material_id)
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
    