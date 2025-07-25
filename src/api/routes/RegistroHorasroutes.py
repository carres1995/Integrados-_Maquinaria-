from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.crud import RegistroHorascrud
from src.schemas.response import RegistroHoras_response
from src.schemas.RegistroHoraschemas import RegistroHorasCreate
from typing import List
from uuid import UUID

router= APIRouter()

@router.get('/', response_model=List[RegistroHoras_response.RegistroHorasResponse])
def read_registro(db:Session = Depends(get_db)):
    return RegistroHorascrud.get_registros_horas(db)

@router.post('/registro_horas/', response_model= RegistroHoras_response.RegistroHorasResponse, status_code= 201)
def create_registro(registro: RegistroHorasCreate,db:Session = Depends(get_db)):
    return RegistroHorascrud.create_registro(db=db, registro=registro)

@router.get('/registro_horas/{registro_id}', response_model=RegistroHoras_response.RegistroHorasResponse)
def get_registro_id(registro_id:UUID,db:Session=Depends(get_db)):
    db_registro= RegistroHorascrud.get_registro_by_id(db=db, registro_id=registro_id)
    if db_registro not in db:
        raise HTTPException (status_code=404, detail='Regitro de horas no encontrado.')
    return db_registro


@router.put("/registro_horas/{registro_id}", response_model=RegistroHoras_response.RegistroHorasResponse)
def update_registro(registro_id: UUID, registro: RegistroHorasCreate, db: Session = Depends(get_db)):
    update = RegistroHorascrud.update_registro(db, registro_id, registro)
    if not update:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return update

@router.delete("/registro_horas/{registro_id}")
def delete_registro(registro_id: UUID, db: Session = Depends(get_db)):
    delete = RegistroHorascrud.delete_registro(db, registro_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"detail": "Registro eliminado correctamente"}
    


