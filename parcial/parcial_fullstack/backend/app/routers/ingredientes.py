from typing import Annotated
from fastapi import APIRouter, Query, Path, status
from app.models import Ingrediente
from app.schemas import IngredienteCreate, IngredienteRead, IngredienteUpdate
from app.services.crud import create_ingrediente, delete_entity, get_or_404, list_entities, update_ingrediente
from app.uow.unit_of_work import SessionDep

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])

@router.get("/", response_model=list[IngredienteRead])
def listar_ingredientes(session: SessionDep, search: Annotated[str | None, Query(min_length=2, max_length=80)] = None, offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=1, le=100)] = 20):
    return list_entities(session, Ingrediente, search, offset, limit)

@router.get("/{ingrediente_id}", response_model=IngredienteRead)
def obtener_ingrediente(session: SessionDep, ingrediente_id: Annotated[int, Path(gt=0)]):
    return get_or_404(session, Ingrediente, ingrediente_id)

@router.post("/", response_model=IngredienteRead, status_code=status.HTTP_201_CREATED)
def crear_ingrediente(data: IngredienteCreate, session: SessionDep):
    return create_ingrediente(session, data)

@router.put("/{ingrediente_id}", response_model=IngredienteRead)
def editar_ingrediente(ingrediente_id: Annotated[int, Path(gt=0)], data: IngredienteUpdate, session: SessionDep):
    return update_ingrediente(session, ingrediente_id, data)

@router.delete("/{ingrediente_id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_ingrediente(ingrediente_id: Annotated[int, Path(gt=0)], session: SessionDep):
    delete_entity(session, Ingrediente, ingrediente_id)
