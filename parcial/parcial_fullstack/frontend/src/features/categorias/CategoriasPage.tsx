import { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { catalogoApi } from '../../api/catalogo';
import type { Categoria } from '../../types/models';
import { Modal } from '../../components/Modal';
import { LoadingError } from '../../components/LoadingError';

const empty = { nombre:'', descripcion:'', activa:true };
export function CategoriasPage(){
 const qc = useQueryClient(); const [open,setOpen]=useState(false); const [edit,setEdit]=useState<Categoria|null>(null); const [form,setForm]=useState(empty);
 const {data=[],isLoading,error}=useQuery({queryKey:['categorias'],queryFn:catalogoApi.categorias});
 const save=useMutation({mutationFn:()=> edit ? catalogoApi.editarCategoria(edit.id,form) : catalogoApi.crearCategoria(form), onSuccess:()=>{qc.invalidateQueries({queryKey:['categorias']}); setOpen(false); setEdit(null); setForm(empty)}});
 const del=useMutation({mutationFn:catalogoApi.borrarCategoria,onSuccess:()=>qc.invalidateQueries({queryKey:['categorias']})});
 function start(c?:Categoria){setEdit(c??null); setForm(c?{nombre:c.nombre,descripcion:c.descripcion??'',activa:c.activa}:empty); setOpen(true)}
 return <section><div className="flex justify-between mb-4"><h2 className="text-2xl font-bold">Categorías</h2><button onClick={()=>start()} className="bg-slate-900 text-white px-4 py-2 rounded-xl">Nueva categoría</button></div><LoadingError isLoading={isLoading} error={error as Error|null}/><div className="bg-white rounded-2xl shadow overflow-hidden"><table className="w-full text-sm"><thead className="bg-slate-100"><tr><th className="p-3 text-left">Nombre</th><th>Descripción</th><th>Estado</th><th>Acciones</th></tr></thead><tbody>{data.map(c=><tr className="border-t" key={c.id}><td className="p-3 font-medium">{c.nombre}</td><td>{c.descripcion}</td><td>{c.activa?'Activa':'Inactiva'}</td><td className="space-x-2"><button onClick={()=>start(c)} className="px-3 py-1 bg-blue-100 rounded-lg">Editar</button><button onClick={()=>del.mutate(c.id)} className="px-3 py-1 bg-red-100 rounded-lg">Eliminar</button></td></tr>)}</tbody></table></div><Modal title={edit?'Editar categoría':'Nueva categoría'} open={open} onClose={()=>setOpen(false)}><form onSubmit={(e)=>{e.preventDefault();save.mutate()}} className="grid gap-3"><input className="border rounded-xl p-2" placeholder="Nombre" minLength={3} value={form.nombre} onChange={e=>setForm({...form,nombre:e.target.value})}/><textarea className="border rounded-xl p-2" placeholder="Descripción" value={form.descripcion} onChange={e=>setForm({...form,descripcion:e.target.value})}/><label className="flex gap-2"><input type="checkbox" checked={form.activa} onChange={e=>setForm({...form,activa:e.target.checked})}/> Activa</label><button className="bg-slate-900 text-white rounded-xl p-2">Guardar</button>{save.error && <p className="text-red-600">{save.error.message}</p>}</form></Modal></section>
}
