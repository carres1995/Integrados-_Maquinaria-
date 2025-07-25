from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.crud import Materialescrud
from src.schemas.response import Material_response
from src.schemas import Materialeschemas
from typing import List
from uuid import UUID

router = APIRouter()

@router.get('/', response_model= List[Material_response.MaterialResponse])
def read_materiales(db:Session = Depends(get_db)):
    return Materialescrud.get_materiales(db)

@router.get('/id/{material_id}', response_model=Material_response.MaterialResponse)
def get_material(material_id: UUID,db: Session = Depends(get_db)):
    db_material = Materialescrud.get_material_id(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail='No se encontro el material')
    return db_material

@router.get('/name/{nombre}', response_model=Material_response.MaterialResponse)
def get_material_by_id(nombre: str,db: Session = Depends(get_db)):
    db_material = Materialescrud.get_material_by_name(db, nombre=nombre)
    if db_material is None:
        raise HTTPException(status_code=404, detail='No se encontro proveedor.')
    return db_material

@router.post('/create_material', response_model=Material_response.MaterialResponse)
def create_material(material: Materialeschemas.MaterialCreate,db: Session = Depends(get_db)):
    db_material = Materialescrud.get_material_by_name(db, nombre=material.nombre_material)
    if db_material:
        raise HTTPException(status_code=400, detail='Material ya esta registrado.')
    
    return Materialescrud.create_material(db=db, material=material)#type: ignore

@router.put("/{material_id}", response_model=Material_response.MaterialResponse)
def update_material(material_id: UUID, material_data: Materialeschemas.MaterialCreate, db: Session = Depends(get_db)):
    update = Materialescrud.update_material(db, material_id, material_data)
    if not update:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return update

@router.delete("/{material_id}")
def delete_material(material_id: UUID, db: Session = Depends(get_db)):
    delete = Materialescrud.delete_material(db, material_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return {"detail": "Material eliminado correctamente"}
    