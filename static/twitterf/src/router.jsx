import { Route, Routes } from 'react-router-dom'
import { Cadastro } from './pages/cadastro/Cadastro'
import { Home } from './pages/home/Home'
import { Tweet } from './pages/home/Tweet'
import { Login } from './pages/login/login'
import { Perfil } from './pages/perfil/Perfil'

export function RouteApp() {
    return (
        <Routes>
            <Route element={<Cadastro />} path='/cadastro' />
            <Route element={<Login />} path='/' />
            <Route element={<Home />} path='/home' />
            <Route element={<Tweet />} path='/tweet/:id' />
            <Route element={<Perfil />} path='/perfil/:id' />
            <Route element={<Perfil />} path='/perfil' />

        </Routes>
    )
}