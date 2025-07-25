from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.crud import Proveedorescrud
from src.schemas.response import Proveedor_response
from src.schemas import Proveedoreschemas
from typing import List
from uuid import UUID

router = APIRouter()

@router.get('/', response_model= List[Proveedor_response.ProveedorResponse])
def read_proveedor(db:Session = Depends(get_db)):
    return Proveedorescrud.get_proveedores(db)

@router.get('/id/{proveedor_id}', response_model=Proveedor_response.ProveedorResponse)
def get_proveedor_id(proveedor_id: UUID,db: Session = Depends(get_db)):
    db_proveedor = Proveedorescrud.get_proveedor_id(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail='No se encontró proveedor')
    return db_proveedor

@router.get('/name/{nombre}', response_model=Proveedor_response.ProveedorResponse)
def get_proveedor_by_name(nombre: str,db: Session = Depends(get_db)):
    db_proveedor = Proveedorescrud.get_proveedor_by_name(db, nombre=nombre)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail='No se encontro proveedor.')
    return db_proveedor

@router.post('/create_proveedor/', response_model=Proveedor_response.ProveedorResponse)
def create_proveedor(proveedor: Proveedoreschemas.ProveedorCreate,db: Session = Depends(get_db)):
    db_proveedor = Proveedorescrud.get_proveedor_by_name(db, nombre=proveedor.nombre)
    if db_proveedor:
        raise HTTPException(status_code=400, detail='Proveedor ya está registrado.')

    return Proveedorescrud.create_proveedor(db=db, proveedor=proveedor)#type: ignore

@router.put("/update/{proveedor_id}", response_model=Proveedor_response.ProveedorResponse)
def update(proveedor_id: UUID, proveedor_data: Proveedoreschemas.ProveedorCreate, db: Session = Depends(get_db)):
    update = Proveedorescrud.update_proveedor(db, proveedor_id, proveedor_data)
    if not update:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return update

@router.delete("/{proveedor_id}")
def delete(proveedor_id: UUID, db: Session = Depends(get_db)):
    delete = Proveedorescrud.delete_proveedor(db, proveedor_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return {"detail": f"Proveedor {proveedor_id} eliminado correctamente"}
    
    

     