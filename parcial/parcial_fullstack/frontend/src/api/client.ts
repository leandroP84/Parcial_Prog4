const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api';

export async function http<T>(path: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, { headers: { 'Content-Type': 'application/json', ...(options.headers ?? {}) }, ...options });
  if (!response.ok) {
    let detail = 'Error en la petición';
    try { const data = await response.json(); detail = data.detail ?? detail; } catch { /* noop */ }
    throw new Error(Array.isArray(detail) ? detail.map((d:any)=>d.msg).join(', ') : detail);
  }
  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}
