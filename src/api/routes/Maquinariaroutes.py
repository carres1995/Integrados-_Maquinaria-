from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.crud import Maquinariacrud
from src.schemas.response import Maquinaria_response
from src.schemas.Maquinariaschemas import MaquinariaCreate
from typing import List
from uuid import UUID

router= APIRouter()

@router.get('/', response_model=List[Maquinaria_response.MaquinariRespose])
def read_maquinaria(db:Session = Depends(get_db)):
    return Maquinariacrud.get_maquinarias(db)

@router.post('/create/', response_model= Maquinaria_response.MaquinariRespose, status_code= 201)
def create_maquinaria(maquinaria: MaquinariaCreate,db:Session = Depends(get_db)):
    return Maquinariacrud.create_maquinaria(db=db, maquinaria=maquinaria)

@router.get('/id/{maquinaria_id}', response_model=Maquinaria_response.MaquinariRespose)
def get_maquinaria_id(maquinaria_id:UUID,db:Session=Depends(get_db)):
    db_registro= Maquinariacrud.get_maquinaria_by_id(db=db, maquinaria_id=maquinaria_id)
    if db_registro not in db:
        raise HTTPException (status_code=404, detail='Maquinaria de horas no encontrado.')
    return db_registro

@router.get('/name/{nombre}', response_model=Maquinaria_response.MaquinariRespose)
def get_maquinaria_name(nombre:str,db:Session=Depends(get_db)):
    db_registro= Maquinariacrud.get_maquinaria_by_name(db=db, nombre=nombre)
    if not db_registro:
        raise HTTPException(status_code=404, detail='Maquinaria no encontrada.')
    return db_registro

@router.put("/update/{maquinaria_id}", response_model=Maquinaria_response.MaquinariRespose)
def update_maquinaria(maquinaria_id: UUID, maquinaria: MaquinariaCreate, db: Session = Depends(get_db)):
    update = Maquinariacrud.update_maquinaria(db, maquinaria_id, maquinaria)
    if not update:
        raise HTTPException(status_code=404, detail="Maquinaria no encontrado")
    return update

@router.delete("/delete/{maquinaria_id}",response_model=Maquinaria_response.MaquinariRespose)
def delete_maquinaria(maquinaria_id: UUID, db: Session = Depends(get_db)):
    delete = Maquinariacrud.delete_maquinaria(db, maquinaria_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Maquinaria no encontrado")
    return delete