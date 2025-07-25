from sqlalchemy.orm import Session
from src.api.dependencies import get_db
from src.models.InstalacionMaterial import InstalacionMaterial
from src.schemas.response.InstalacionMaterial_response import InstalacionMaterialResponse
from src.schemas.InstalacionMaterialeschemas import InstalacionMaterialCreate
from typing import List
from src.crud import InstalacionMaterialcrud
from fastapi import APIRouter, Depends,HTTPException
from uuid import UUID

router=APIRouter()

@router.get('/Instalaciones_materiales/', response_model=List[InstalacionMaterialResponse])
def get_instalaciones_all(db:Session = Depends(get_db)):
    return InstalacionMaterialcrud.get_instalacion_material_all(db)

@router.get('/instalacion_material/{instalacion_id}', response_model= InstalacionMaterialResponse)
def get_instalacion_by_id(instalacion_id: UUID, db:Session = Depends(get_db)):
    db_instalacion= InstalacionMaterialcrud.get_instalacion_material_by_id(db=db, instalacion_id= instalacion_id)
    if db_instalacion not in db:
        raise HTTPException (status_code=404,detail='Instalacion material no encontrada. ')
    return db_instalacion

@router.post('/intalacion_material/', response_model=InstalacionMaterialResponse)
def create_instalacion_material(instalacion: InstalacionMaterialCreate ,db:Session = Depends(get_db)):
    return InstalacionMaterialcrud.create_instalacion_material(db=db,instalacion=instalacion)

@router.put('/instalacion_material/{instalacion_id}', response_model=InstalacionMaterialResponse)
def update_instalacion_material(instalacion_id:UUID , instalacion: InstalacionMaterialCreate ,db:Session = Depends(get_db)):
    update= InstalacionMaterialcrud.update_instalacion_material(db, instalacion_id,instalacion)
    if update not in db:
        raise HTTPException (status_code=404, detail='Instalacion no encontrada.')
    return update

@router.delete('/instalacion_material/{instalacion_id}', response_model=InstalacionMaterialResponse)
def delete_instalacion(instalacion_id:UUID, db:Session = Depends(get_db)):
    delete= InstalacionMaterialcrud.delete_instalacion_material(db, instalacion_id)
    if delete not in db:
        raise HTTPException (status_code=404, detail='Instalacion no encontrada.')
    return {"detail": f"Instalacion {instalacion_id} eliminada correctamente"}
