# Parcial 1 - Programación 4

Proyecto fullstack realizado para la Tecnicatura Universitaria en Programación: API con FastAPI + SQLModel + PostgreSQL y frontend con React + TypeScript + Tailwind CSS 4 + TanStack Query.

## Módulos implementados

- Categorías
- Ingredientes
- Productos
- ProductoCategoria, relación muchos a muchos entre Producto y Categoría
- ProductoIngrediente, relación muchos a muchos entre Producto e Ingrediente

## Requisitos

- Python 3.11 o superior
- Node.js 20 o superior
- Docker Desktop o PostgreSQL instalado localmente

## Ejecución del backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
cd ..
docker compose up -d
cd backend
fastapi dev app/main.py
```

La API queda en:

- http://localhost:8000
- http://localhost:8000/docs

Para cargar datos de ejemplo:

```bash
cd backend
python -m app.seed
```

## Ejecución del frontend

```bash
cd frontend
npm install
npm run dev
```

La app queda en:

- http://localhost:5173

## Arquitectura

El backend está organizado por capas:

- `models`: entidades SQLModel y relaciones con `Relationship` y `link_model`.
- `schemas`: modelos de entrada y salida usados con `response_model`.
- `routers`: endpoints HTTP con `Annotated`, `Query` y `Path`.
- `services`: lógica de negocio, validación de relaciones y CRUD.
- `uow`: dependencia de sesión de base de datos.
- `core`: configuración y conexión a PostgreSQL.

El frontend usa:

- `react-router-dom` para navegación SPA.
- Ruta dinámica `/productos/:id` para ver detalle.
- `useQuery` para listados y detalle.
- `useMutation` para crear, editar y eliminar.
- `invalidateQueries` para sincronizar la interfaz después de cada cambio.
- Tailwind CSS 4 para diseño responsive.

## Link al video

Agregar acá el link al video de YouTube oculto o Drive:

`PEGAR_LINK_DEL_VIDEO_AQUI`
