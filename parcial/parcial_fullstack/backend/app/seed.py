from sqlmodel import Session, select
from app.core.database import engine, create_db_and_tables
from app.models import Categoria, Ingrediente, Producto


def run():
    create_db_and_tables()
    with Session(engine) as session:
        if session.exec(select(Categoria)).first():
            print("La base ya tiene datos.")
            return
        c1 = Categoria(nombre="Bebidas", descripcion="Productos líquidos")
        c2 = Categoria(nombre="Comidas", descripcion="Productos elaborados")
        i1 = Ingrediente(nombre="Harina", unidad_medida="kg", stock=20, es_alergeno=True)
        i2 = Ingrediente(nombre="Tomate", unidad_medida="kg", stock=15, es_alergeno=False)
        p1 = Producto(nombre="Pizza muzzarella", descripcion="Producto de ejemplo", precio=8500, categorias=[c2], ingredientes=[i1, i2])
        session.add(p1)
        session.commit()
        print("Datos iniciales cargados.")

if __name__ == "__main__":
    run()
