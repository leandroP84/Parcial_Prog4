from typing import Annotated
from fastapi import APIRouter, Query, Path, status
from app.models import Producto
from app.schemas import ProductoCreate, ProductoRead, ProductoUpdate
from app.services.crud import create_producto, delete_entity, get_or_404, list_entities, update_producto
from app.uow.unit_of_work import SessionDep

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=list[ProductoRead])
def listar_productos(session: SessionDep, search: Annotated[str | None, Query(min_length=2, max_length=80)] = None, offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=1, le=100)] = 20):
    return list_entities(session, Producto, search, offset, limit)

@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(session: SessionDep, producto_id: Annotated[int, Path(gt=0)]):
    return get_or_404(session, Producto, producto_id)

@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate, session: SessionDep):
    return create_producto(session, data)

@router.put("/{producto_id}", response_model=ProductoRead)
def editar_producto(producto_id: Annotated[int, Path(gt=0)], data: ProductoUpdate, session: SessionDep):
    return update_producto(session, producto_id, data)

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_producto(producto_id: Annotated[int, Path(gt=0)], session: SessionDep):
    delete_entity(session, Producto, producto_id)
