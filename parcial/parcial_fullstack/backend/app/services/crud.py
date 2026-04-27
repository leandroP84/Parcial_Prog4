from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from app.models import Categoria, Ingrediente, Producto
from app.schemas import (
    CategoriaCreate, CategoriaUpdate, IngredienteCreate, IngredienteUpdate,
    ProductoCreate, ProductoUpdate,
)


def _commit_or_400(session: Session, obj):
    try:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe un registro con esos datos") from exc


def list_entities(session: Session, model, search: str | None, offset: int, limit: int):
    statement = select(model)
    if search:
        statement = statement.where(model.nombre.ilike(f"%{search}%"))
    return session.exec(statement.offset(offset).limit(limit)).all()


def get_or_404(session: Session, model, item_id: int):
    obj = session.get(model, item_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{model.__name__} no encontrado")
    return obj


def create_categoria(session: Session, data: CategoriaCreate):
    return _commit_or_400(session, Categoria.model_validate(data))


def update_categoria(session: Session, item_id: int, data: CategoriaUpdate):
    obj = get_or_404(session, Categoria, item_id)
    obj.sqlmodel_update(data.model_dump(exclude_unset=True))
    return _commit_or_400(session, obj)


def create_ingrediente(session: Session, data: IngredienteCreate):
    return _commit_or_400(session, Ingrediente.model_validate(data))


def update_ingrediente(session: Session, item_id: int, data: IngredienteUpdate):
    obj = get_or_404(session, Ingrediente, item_id)
    obj.sqlmodel_update(data.model_dump(exclude_unset=True))
    return _commit_or_400(session, obj)


def _resolve_many(session: Session, model, ids: list[int]):
    if not ids:
        return []
    rows = session.exec(select(model).where(model.id.in_(ids))).all()
    if len(rows) != len(set(ids)):
        raise HTTPException(status_code=404, detail=f"Hay IDs inexistentes en {model.__name__}")
    return rows


def create_producto(session: Session, data: ProductoCreate):
    payload = data.model_dump(exclude={"categoria_ids", "ingrediente_ids"})
    obj = Producto.model_validate(payload)
    obj.categorias = _resolve_many(session, Categoria, data.categoria_ids)
    obj.ingredientes = _resolve_many(session, Ingrediente, data.ingrediente_ids)
    return _commit_or_400(session, obj)


def update_producto(session: Session, item_id: int, data: ProductoUpdate):
    obj = get_or_404(session, Producto, item_id)
    values = data.model_dump(exclude_unset=True, exclude={"categoria_ids", "ingrediente_ids"})
    obj.sqlmodel_update(values)
    if data.categoria_ids is not None:
        obj.categorias = _resolve_many(session, Categoria, data.categoria_ids)
    if data.ingrediente_ids is not None:
        obj.ingredientes = _resolve_many(session, Ingrediente, data.ingrediente_ids)
    return _commit_or_400(session, obj)


def delete_entity(session: Session, model, item_id: int) -> None:
    obj = get_or_404(session, model, item_id)
    session.delete(obj)
    session.commit()
