import { http } from './client';
import type { Categoria, Ingrediente, Producto, ProductoPayload } from '../types/models';
export const catalogoApi = {
  categorias: () => http<Categoria[]>('/categorias/'),
  crearCategoria: (data: Omit<Categoria,'id'>) => http<Categoria>('/categorias/', { method:'POST', body: JSON.stringify(data) }),
  editarCategoria: (id:number, data: Partial<Omit<Categoria,'id'>>) => http<Categoria>(`/categorias/${id}`, { method:'PUT', body: JSON.stringify(data) }),
  borrarCategoria: (id:number) => http<void>(`/categorias/${id}`, { method:'DELETE' }),
  ingredientes: () => http<Ingrediente[]>('/ingredientes/'),
  crearIngrediente: (data: Omit<Ingrediente,'id'>) => http<Ingrediente>('/ingredientes/', { method:'POST', body: JSON.stringify(data) }),
  editarIngrediente: (id:number, data: Partial<Omit<Ingrediente,'id'>>) => http<Ingrediente>(`/ingredientes/${id}`, { method:'PUT', body: JSON.stringify(data) }),
  borrarIngrediente: (id:number) => http<void>(`/ingredientes/${id}`, { method:'DELETE' }),
  productos: () => http<Producto[]>('/productos/'),
  producto: (id:number) => http<Producto>(`/productos/${id}`),
  crearProducto: (data: ProductoPayload) => http<Producto>('/productos/', { method:'POST', body: JSON.stringify(data) }),
  editarProducto: (id:number, data: Partial<ProductoPayload>) => http<Producto>(`/productos/${id}`, { method:'PUT', body: JSON.stringify(data) }),
  borrarProducto: (id:number) => http<void>(`/productos/${id}`, { method:'DELETE' }),
};
