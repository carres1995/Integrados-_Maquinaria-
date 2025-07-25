from sqlalchemy.orm import Session
from src.models.Proveedores import Proveedores
from src.schemas.Proveedoreschemas import ProveedorCreate
from uuid import UUID

def get_proveedores(db:Session):
    return db.query(Proveedores).all()

def get_proveedor_id(db:Session, proveedor_id: UUID):
    return db.query(Proveedores).filter(Proveedores.id == proveedor_id).first()

def get_proveedor_by_name(db:Session, nombre: str):
    return db.query(Proveedores).filter(Proveedores.nombre == nombre).first()

def create_proveedor(db:Session, proveedor:ProveedorCreate):
    db_proveedor = Proveedores(
        nombre=proveedor.nombre,
        direccion=proveedor.direccion,
        telefono=proveedor.telefono,
        email=proveedor.email
    )
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def update_proveedor(db: Session, proveedor_id:UUID, proveedor_data: ProveedorCreate):
    db_proveedor = get_proveedor_id(db, proveedor_id)
    if db_proveedor:
        db_proveedor.nombre = proveedor_data.nombre #type: ignore
        db_proveedor.direccion = proveedor_data.direccion #type: ignore
        db_proveedor.telefono = proveedor_data.telefono #type: ignore
        db_proveedor.email = proveedor_data.email #type: ignore
        db.commit()
        db.refresh(db_proveedor)
    return db_proveedor

def delete_proveedor(db: Session, proveedor_id):
    db_proveedor = get_proveedor_id(db, proveedor_id)
    if db_proveedor:
        db.delete(db_proveedor)
        db.commit()
    return db_proveedor
    
    




    

