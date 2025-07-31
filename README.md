 Sistema Integrado de Gestión de Maquinaria

Sistema backend modular desarrollado en Python para administrar eficientemente:
- Operación de maquinaria pesada
- Registro de horas máquina y horas hombre
- Mantenimiento preventivo y correctivo
- Control e instalación de repuestos y materiales
- Gestión de proveedores
- Seguimiento del personal operativo y técnico


---

## Objetivos del Proyecto

1. Centralizar toda la información operativa y técnica de la maquinaria.
2. Registrar horas trabajadas por máquinas y personas, discriminando actividades.
3. Llevar control de mantenimiento preventivo/correctivo por máquina.
4. Monitorear repuestos y su vida útil por horas.
5. Facilitar reportes por máquina o persona para nómina y decisiones operativas.
6. Enviar alertas desde CLI por eventos importantes (ej: stock mínimo).

---

##  Módulos y Funcionalidades

### 1. Registro de Maquinaria
**Objetivo:** Gestionar toda la información de las máquinas.

**Funciones principales:**
- Crear, consultar, editar y eliminar registros (CRUD).
- Asignar ubicación (frente, centro de trabajo, zona).
- Consultar historial de mantenimiento y uso.
- Asignar componentes instalados y actualizar su estado.
- Adjuntar documentos (nombre del archivo o ruta para CLI).

**Campos necesarios:**
- Código único interno
- Nombre o tipo de máquina
- Marca / Modelo
- Año / Fecha de adquisición
- Estado operativo (`Operativa`, `En mantenimiento`, `Fuera de servicio`)
- Ubicación actual
- Observaciones técnicas

---

### 2. Mantenimientos (Preventivo y Correctivo)
**Objetivo:** Registrar intervenciones técnicas con detalle y seguimiento.

**Funciones principales:**
- Registrar mantenimientos con tipo, fecha y responsable.
- Ver mantenimientos anteriores por máquina.
- Asignar repuestos usados.
- Generar historial por técnico, máquina o rango de fechas.

**Campos necesarios:**
- ID de máquina
- Tipo (`Preventivo` o `Correctivo`)
- Fecha de inicio y fin
- Técnico responsable
- Diagnóstico / observaciones
- Repuestos usados (lista)
- Costo estimado o real
- Archivo adjunto (opcional, como texto/ruta CLI)

---

### 3. Repuestos y Materiales
**Objetivo:** Controlar el inventario de insumos técnicos.

**Funciones principales:**
- Crear, editar, eliminar y consultar artículos (CRUD).
- Registrar entradas y salidas de stock.
- Asociar repuestos a mantenimientos y máquinas.
- Configurar stock mínimo, actual y máximo.
- Generar alertas por stock bajo.

**Campos necesarios:**
- Código interno
- Nombre del repuesto
- Categoría (motor, eléctrico, hidráulico, etc.)
- Unidad de medida
- Precio unitario
- Stock actual / mínimo / máximo
- Proveedor asociado
- Historial de movimientos (fecha, entrada/salida, cantidad)

---

### 4. Proveedores
**Objetivo:** Llevar registro de empresas o personas que suministran materiales.

**Funciones principales:**
- CRUD completo de proveedores.
- Ver historial de entregas por proveedor.
- Asociar proveedor a uno o varios repuestos.

**Campos necesarios:**
- Nombre comercial
- NIT o número de identificación
- Dirección
- Teléfono
- Correo electrónico
- Persona de contacto
- Lista de productos suministrados

---

### 5. Registro de Horas Máquina y Horas Hombre
**Objetivo:** Documentar el uso diario de las máquinas y las horas trabajadas por el personal.

**Funciones principales:**
- CRUD de registros de horas por persona y máquina.
- Clasificar horas por tipo de actividad.
- Asociar operador, máquina y tipo de trabajo.
- Consultar reportes por persona o máquina.
- Exportar informe (opcionalmente como `.csv` o `.txt` desde CLI).

**Campos necesarios:**
- Fecha
- Máquina utilizada
- Persona asignada (operador, ayudante, técnico)
- Horas trabajadas
- Tipo de actividad:  
  - `Producción`  
  - `Mantenimiento`  
  - `Parada por falla`  
  - `Parada programada`  
  - `Transporte`  
  - `Otro`
- Observaciones
- Turno (si aplica)

**Informes requeridos:**
- Total de horas por máquina en un rango de fechas.
- Total de horas por persona para nómina.
- Horas por tipo de actividad.
- Indicadores de eficiencia (horas productivas vs. paradas).

---

### 6. Personal
**Objetivo:** Mantener control del personal operativo y técnico.

**Funciones principales:**
- CRUD completo del personal.
- Asignar rol: `Operador`, `Ayudante`, `Técnico`, `Mecánico`.
- Consultar historial de trabajos realizados.
- Filtrar por estado (`Activo`, `Inactivo`) y por cargo.

**Campos necesarios:**
- Nombre completo
- Documento de identidad
- Cargo/Rol
- Fecha de ingreso
- Estado (activo/inactivo)
- Teléfono
- Correo electrónico

---

### 7. Componentes Instalados y Vida Útil
**Objetivo:** Controlar los repuestos o partes instaladas en máquinas y su desgaste por horas.

**Funciones principales:**
- Registrar instalación de componente en una máquina.
- Registrar fecha y hora de instalación.
- Configurar vida útil estimada en horas.
- Asociar con repuesto y proveedor.
- Almacenar horas acumuladas de uso.
- Generar alerta cuando se alcanza vida útil.

**Campos necesarios:**
- Máquina asociada
- Código y nombre del componente
- Fecha de instalación
- Vida útil en horas
- Horas acumuladas (se actualiza automáticamente con las horas máquina)
- Estado: `Operativo`, `Por reemplazar`, `Vencido`

---

## 8. Dashboard (vía CLI o futura GUI)

**Resumen generado desde consola o pantalla principal:**
- Total de máquinas registradas
- Máquinas activas / inactivas
- Mantenimientos programados hoy/semana
- Repuestos con stock bajo
- Horas trabajadas esta semana (por persona y por máquina)
- Alertas activas (vida útil, stock mínimo, etc.)






