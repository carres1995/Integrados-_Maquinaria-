from sqlalchemy.orm import Session
from src.models.RegistroHoras import RegistroHoras
from src.schemas.RegistroHoraschemas import RegistroHorasCreate
from uuid import UUID

def get_registros_horas(db: Session):
    return db.query(RegistroHoras).all()

def get_registro_by_id(db:Session, registro_id: UUID):
    return db.query(RegistroHoras).filter(RegistroHoras.id == registro_id).first()

def get_registro_by_actividad(db:Session, registro_act: str):
    return db.query(RegistroHoras).filter(RegistroHoras.actividad== registro_act).first()

def create_registro(db:Session, registro:RegistroHorasCreate):
    db_registro= RegistroHoras(
        maquinaria_id = registro.maquinaria_id,
        fecha = registro.fecha,
        horas_maquina = registro.horas_maquina,
        actividad = registro.actividad,
        operador = registro.operador
        )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

def update_registro(db:Session, registro_id: UUID,registro:RegistroHorasCreate):
    db_registro =get_registro_by_id(db, registro_id)
    if db_registro:
        db_registro.maquinaria_id= registro.maquinaria_id,#type: ignore
        db_registro.fecha= registro.fecha,#type: ignore
        db_registro.horas_maquina= registro.horas_maquina,#type: ignore
        db_registro.actividad= registro.actividad,#type: ignore
        db_registro.operador= registro.operador,#type: ignore
        
        db.commit()
        db.refresh(db_registro)
    return db_registro

def delete_registro(db:Session, registro_id:UUID):
    db_registro =get_registro_by_id(db, registro_id)
    if db_registro:
        db.delete(db_registro)
        db.commit()
    return db_registro    