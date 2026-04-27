# Lista de Verificación del Proyecto Integrador

## Backend (FastAPI + SQLModel)
- [x] Entorno: Uso de .venv, requirements.txt y FastAPI funcionando en modo dev.
- [x] Modelado: Tablas creadas con SQLModel incluyendo relaciones Relationship (1:N y N:N).
- [x] Validación: Uso de Annotated, Query y Path para reglas de negocio.
- [x] CRUD Persistente: Endpoints funcionales para Crear, Leer, Actualizar y Borrar en PostgreSQL.
- [x] Seguridad de Datos: Implementación de response_model para no filtrar datos innecesarios.
- [x] Estructura: Código organizado por módulos: routers, schemas, services, models, uow y core.

## Frontend (React + TypeScript + Tailwind)
- [x] Setup: Proyecto creado con Vite + TS y estructura de carpetas limpia.
- [x] Componentes: Uso de componentes funcionales y Props tipadas con interfaces.
- [x] Estilos: Interfaz construida con clases de utilidad de Tailwind CSS 4.
- [x] Navegación: Configuración de react-router-dom con ruta dinámica /productos/:id.
- [x] Estado Local: Uso de useState para formularios y modales.

## Integración y Server State
- [x] Lectura (useQuery): Listados y detalles consumiendo datos reales de la API.
- [x] Escritura (useMutation): Formularios que envían datos al backend.
- [x] Sincronización: Uso de invalidateQueries después de crear, editar y borrar.
- [x] Feedback: Gestión visual de Cargando y Error.

## Video de Presentación
- [ ] Duración: El video dura 15 minutos o menos.
- [ ] Audio/Video: La voz es clara y la resolución permite leer el código.
- [ ] Demo: Se muestra el flujo completo desde la creación hasta la persistencia en DB.
