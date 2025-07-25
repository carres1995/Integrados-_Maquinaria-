from sqlalchemy.orm import Session
from src.models.Mantenimiento import Mantenimiento
from src.schemas.Mantenimientoschemas import MantenimientosCreate
from uuid import UUID

def get_mantenimiento(db: Session):
    return db.query(Mantenimiento).all()

def get_mantenimiento_by_id(db:Session, mantenimiento_id: UUID):
    return db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()

def create_mantenimiento(db:Session, mantenimiento:MantenimientosCreate):
    db_mantenimiento= Mantenimiento(
        maquinaria_id = mantenimiento.maquinaria_id,
        tipo_mantenimiento = mantenimiento.tipo_mantenimiento,
        fecha_inicio = mantenimiento.fecha_inicio,
        fecha_fin = mantenimiento.fecha_fin,
        descripcion = mantenimiento.descripcion,
        responsable = mantenimiento.responsable,
        estado = mantenimiento.estado
        )
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)
    return db_mantenimiento

def update_mantenimiento(db:Session, mantenimiento_id: UUID,mantenimiento:MantenimientosCreate):
    db_mantenimiento =get_mantenimiento_by_id(db, mantenimiento_id)
    if db_mantenimiento:
        db_mantenimiento.maquinaria_id= mantenimiento.maquinaria_id,# type: ignore 
        db_mantenimiento.tipo_mantenimiento= mantenimiento.tipo_mantenimiento,#type: ignore
        db_mantenimiento.fecha_inicio= mantenimiento.fecha_inicio,#type: ignore
        db_mantenimiento.fecha_fin= mantenimiento.fecha_fin,#type: ignore
        db_mantenimiento.descripcion= mantenimiento.descripcion,#type: ignore
        db_mantenimiento.responsable= mantenimiento.responsable,#type: ignore
        db_mantenimiento.estado= mantenimiento.estado,#type: ignore
        
        db.commit()
        db.refresh(db_mantenimiento)
    return db_mantenimiento

def delete_mantenimiento(db:Session, mantenimiento_id:UUID):
    db_mantenimiento =get_mantenimiento_by_id(db, mantenimiento_id)
    if db_mantenimiento:
        db.delete(db_mantenimiento)
        db.commit()
    return db_mantenimiento    