from sqlalchemy.orm import Session
from src.models.Maquinaria import Maquinaria
from src.schemas.Maquinariaschemas import MaquinariaCreate
from uuid import UUID

def get_maquinarias(db: Session):
    return db.query(Maquinaria).all()

def get_maquinaria_by_id(db:Session, maquinaria_id: UUID):
    return db.query(Maquinaria).filter(Maquinaria.id == maquinaria_id).first()

def get_maquinaria_by_name(db:Session, nombre: str):
    return db.query(Maquinaria).filter(Maquinaria.nombre== nombre).first()

def create_maquinaria(db:Session, maquinaria:MaquinariaCreate):
    db_maquinaria= Maquinaria(
        nombre = maquinaria.nombre,
        tipo = maquinaria.tipo,
        modelo = maquinaria.modelo,
        serie = maquinaria.serie,
        ubicacion = maquinaria.ubicacion,
        fecha_adquisicion= maquinaria.fecha_adquisicion,
        estado=maquinaria.estado
        )
    db.add(db_maquinaria)
    db.commit()
    db.refresh(db_maquinaria)
    return db_maquinaria

def update_maquinaria(db:Session, maquinaria_id: UUID,maquinaria:MaquinariaCreate):
    db_maquinaria =get_maquinaria_by_id(db, maquinaria_id)
    if db_maquinaria:
        db_maquinaria.nombre= maquinaria.nombre,# type: ignore #type: ignore
        db_maquinaria.tipo= maquinaria.tipo,#type: ignore
        db_maquinaria.modelo= maquinaria.modelo,#type: ignore
        db_maquinaria.serie= maquinaria.serie,#type: ignore
        db_maquinaria.ubicacion= maquinaria.ubicacion,#type: ignore
        db_maquinaria.fecha_adquisicion= maquinaria.fecha_adquisicion,#type: ignore
        db_maquinaria.estado= maquinaria.estado,#type: ignore
        
        db.commit()
        db.refresh(db_maquinaria)
    return db_maquinaria

def delete_maquinaria(db:Session, maquinaria_id:UUID):
    db_maquinaria =get_maquinaria_by_id(db, maquinaria_id)
    if db_maquinaria:
        db.delete(db_maquinaria)
        db.commit()
    return db_maquinaria    