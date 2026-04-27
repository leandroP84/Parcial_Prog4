from typing import Annotated
from fastapi import APIRouter, Query, Path, status
from app.models import Categoria
from app.schemas import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.services.crud import create_categoria, delete_entity, get_or_404, list_entities, update_categoria
from app.uow.unit_of_work import SessionDep

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/", response_model=list[CategoriaRead])
def listar_categorias(session: SessionDep, search: Annotated[str | None, Query(min_length=2, max_length=80)] = None, offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=1, le=100)] = 20):
    return list_entities(session, Categoria, search, offset, limit)

@router.get("/{categoria_id}", response_model=CategoriaRead)
def obtener_categoria(session: SessionDep, categoria_id: Annotated[int, Path(gt=0)]):
    return get_or_404(session, Categoria, categoria_id)

@router.post("/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(data: CategoriaCreate, session: SessionDep):
    return create_categoria(session, data)

@router.put("/{categoria_id}", response_model=CategoriaRead)
def editar_categoria(categoria_id: Annotated[int, Path(gt=0)], data: CategoriaUpdate, session: SessionDep):
    return update_categoria(session, categoria_id, data)

@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_categoria(categoria_id: Annotated[int, Path(gt=0)], session: SessionDep):
    delete_entity(session, Categoria, categoria_id)
