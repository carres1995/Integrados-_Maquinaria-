from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.crud import Mantenimientocrud
from src.schemas.response import Mantenimiento_response
from src.schemas.Mantenimientoschemas import MantenimientosCreate
from typing import List
from uuid import UUID

router= APIRouter()

@router.get('/', response_model=List[Mantenimiento_response.MantenimientoResponse])
def read_mantenimientos(db:Session = Depends(get_db)):
    return Mantenimientocrud.get_mantenimiento(db)

@router.post('/mantenimiento/', response_model= Mantenimiento_response.MantenimientoResponse, status_code= 201)
def create_mantenimiento(mantenimiento: MantenimientosCreate,db:Session = Depends(get_db)):
    return Mantenimientocrud.create_mantenimiento(db=db, mantenimiento=mantenimiento)

@router.get('/mantenimiento/{mantenimiento_id}', response_model=Mantenimiento_response.MantenimientoResponse)
def get_mantenimiento_id(mantenimiento_id:UUID,db:Session=Depends(get_db)):
    db_mantenimiento= Mantenimientocrud.get_mantenimiento_by_id(db=db, mantenimiento_id=mantenimiento_id)
    if db_mantenimiento not in db:
        raise HTTPException (status_code=404, detail='Mantenimiento no encontrado.')
    return db_mantenimiento


@router.put("/mantenimiento/{mantenimiento_id}", response_model=Mantenimiento_response.MantenimientoResponse)
def update_mantenimiento(mantenimiento_id: UUID, mantenimiento: MantenimientosCreate, db: Session = Depends(get_db)):
    update = Mantenimientocrud.update_mantenimiento(db, mantenimiento_id, mantenimiento)
    if not update:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return update

@router.delete("/mantenimiento/{mantenimiento_id}", response_model=Mantenimiento_response.MantenimientoResponse)
def delete_mantenimiento(mantenimiento_id: UUID, db: Session = Depends(get_db)):
    delete = Mantenimientocrud.delete_mantenimiento(db, mantenimiento_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return {"detail": "Mantenimiento eliminado correctamente"}
    


