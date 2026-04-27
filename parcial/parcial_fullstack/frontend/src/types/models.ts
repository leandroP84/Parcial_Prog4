export interface Categoria { id: number; nombre: string; descripcion?: string | null; activa: boolean; }
export interface Ingrediente { id: number; nombre: string; unidad_medida: string; stock: number; es_alergeno: boolean; }
export interface Producto { id: number; nombre: string; descripcion?: string | null; precio: number; activo: boolean; categorias: Categoria[]; ingredientes: Ingrediente[]; }
export interface ProductoPayload { nombre: string; descripcion?: string; precio: number; activo: boolean; categoria_ids: number[]; ingrediente_ids: number[]; }
