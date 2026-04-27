from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

class ProductoCategoriaLink(SQLModel, table=True):
    __tablename__ = "producto_categoria"
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True)
    categoria_id: Optional[int] = Field(default=None, foreign_key="categoria.id", primary_key=True)

class ProductoIngredienteLink(SQLModel, table=True):
    __tablename__ = "producto_ingrediente"
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True)
    ingrediente_id: Optional[int] = Field(default=None, foreign_key="ingrediente.id", primary_key=True)

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=3, max_length=80, unique=True)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    activa: bool = Field(default=True)

    productos: list["Producto"] = Relationship(back_populates="categorias", link_model=ProductoCategoriaLink)

class Ingrediente(SQLModel, table=True):
    __tablename__ = "ingrediente"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=3, max_length=80, unique=True)
    unidad_medida: str = Field(default="unidad", min_length=2, max_length=30)
    stock: float = Field(default=0, ge=0)
    es_alergeno: bool = Field(default=False)

    productos: list["Producto"] = Relationship(back_populates="ingredientes", link_model=ProductoIngredienteLink)

class Producto(SQLModel, table=True):
    __tablename__ = "producto"
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=3, max_length=80, unique=True)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    precio: float = Field(gt=0)
    activo: bool = Field(default=True)

    categorias: list[Categoria] = Relationship(back_populates="productos", link_model=ProductoCategoriaLink)
    ingredientes: list[Ingrediente] = Relationship(back_populates="productos", link_model=ProductoIngredienteLink)
