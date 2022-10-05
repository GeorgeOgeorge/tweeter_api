import path from 'path'
import {Route, Routes} from 'react-router-dom'
import { Cadastro } from './pages/cadastro/Cadastro'
import { Home } from './pages/home/Home'
import { Login } from './pages/login/login'

export function RouteApp() {
    return (
        <div>
            <Routes>
                <Route element={<Cadastro/>} path='/cadastro'/>
                <Route element={<Login/>} path='/'/>
                <Route element={<Home/>} path='/home'/>
            </Routes>
        </div>
    )
}