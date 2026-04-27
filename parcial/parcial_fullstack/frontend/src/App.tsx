import { Navigate, createBrowserRouter, RouterProvider } from 'react-router-dom';
import { Layout } from './components/Layout';
import { CategoriasPage } from './features/categorias/CategoriasPage';
import { IngredientesPage } from './features/ingredientes/IngredientesPage';
import { ProductosPage } from './features/productos/ProductosPage';
import { ProductoDetallePage } from './features/productos/ProductoDetallePage';
const router=createBrowserRouter([{path:'/',element:<Layout/>,children:[{index:true,element:<Navigate to="/productos"/>},{path:'categorias',element:<CategoriasPage/>},{path:'ingredientes',element:<IngredientesPage/>},{path:'productos',element:<ProductosPage/>},{path:'productos/:id',element:<ProductoDetallePage/>}]}]);
export default function App(){return <RouterProvider router={router}/>}
