from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import Proveedoresroutes,Materialesroutes, RegistroHorasroutes,Maquinariaroutes, Mantenimientoroutes, InstalacionMaterialroutes

from src.db import base

print("URL de la base de datos cargada:", settings.DATABASE_URL)


app= FastAPI(title=settings.PROYECT_NAME, version=settings.PROYECT_VERSION)

app.include_router(Proveedoresroutes.router, prefix='/proveedores', tags= ['Etiquetas [proveedores]'])
app.include_router(Materialesroutes.router, prefix='/materiales', tags=['Etiquetas [Materiales]'])
app.include_router(RegistroHorasroutes.router, prefix='/RegistroHoras', tags= ['Etiquetas [Registro_Horas]'])
app.include_router(Maquinariaroutes.router, prefix='/Maquinaria', tags= ['Etiquetas [Maquinaria]'])
app.include_router(Mantenimientoroutes.router, prefix='/Mantenimiento', tags= ['Etiquetas [Mantenimiento]'])
app.include_router(InstalacionMaterialroutes.router, prefix='/InstalacionMateriales', tags=['Etiquetas [Instalacion_Materiales]'])