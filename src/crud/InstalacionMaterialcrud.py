from sqlalchemy.orm import Session
from uuid import UUID
from src.schemas.InstalacionMaterialeschemas import InstalacionMaterialCreate
from src.models.InstalacionMaterial import InstalacionMaterial


def get_instalacion_material_all(db:Session):
    return db.query(InstalacionMaterial).all()

def get_instalacion_material_by_id(db:Session, instalacion_id: UUID):
    return db.query(InstalacionMaterial).filter(InstalacionMaterial.id == instalacion_id).first()

def create_instalacion_material(db:Session, instalacion: InstalacionMaterialCreate):
    db_instalacion= InstalacionMaterial(
        materiales_id= instalacion.materiales_id,
        maquinaria_id= instalacion.maquinaria_id,
        cantidad= instalacion.cantidad,
        fecha_instalacion= instalacion.fecha_instalacion,
        horas_maquina= instalacion.horas_maquina,
        responsable=instalacion.responsable,
        estado= instalacion.estado
    )
    db.add(db_instalacion)
    db.commit()
    db.refresh(db_instalacion)
    return db_instalacion

def update_instalacion_material(db:Session, instalacion_id: UUID, instalacion: InstalacionMaterialCreate):
    db_instalacion= get_instalacion_material_by_id(db, instalacion_id)
    if db_instalacion:
        db_instalacion.materiales_id=instalacion.materiales_id #type: ignore
        db_instalacion.maquinaria_id=instalacion.maquinaria_id #type: ignore
        db_instalacion.cantidad=instalacion.cantidad #type: ignore
        db_instalacion.fecha_instalacion= instalacion.fecha_instalacion #type: ignore
        db_instalacion.horas_maquina=instalacion.horas_maquina #type: ignore
        db_instalacion.responsable=instalacion.responsable #type: ignore
        db_instalacion.estado= instalacion.estado #type: ignore
        db.commit()
        db.refresh(db_instalacion)
        return db_instalacion

def delete_instalacion_material(db:Session, instalacion_id:UUID):
    db_instalacion= get_instalacion_material_by_id(db,instalacion_id)
    db.delete(db_instalacion)
    db.commit()
    return db_instalacion    