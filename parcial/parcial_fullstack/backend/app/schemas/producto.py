from typing import Optional
from sqlmodel import SQLModel

class CategoriaBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    activa: bool = True

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    activa: Optional[bool] = None

class CategoriaRead(CategoriaBase):
    id: int

class IngredienteBase(SQLModel):
    nombre: str
    unidad_medida: str = "unidad"
    stock: float = 0
    es_alergeno: bool = False

class IngredienteCreate(IngredienteBase):
    pass

class IngredienteUpdate(SQLModel):
    nombre: Optional[str] = None
    unidad_medida: Optional[str] = None
    stock: Optional[float] = None
    es_alergeno: Optional[bool] = None

class IngredienteRead(IngredienteBase):
    id: int

class ProductoBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    activo: bool = True

class ProductoCreate(ProductoBase):
    categoria_ids: list[int] = []
    ingrediente_ids: list[int] = []

class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    activo: Optional[bool] = None
    categoria_ids: Optional[list[int]] = None
    ingrediente_ids: Optional[list[int]] = None

class ProductoRead(ProductoBase):
    id: int
    categorias: list[CategoriaRead] = []
    ingredientes: list[IngredienteRead] = []
