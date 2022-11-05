import { useEffect } from "react";
import { useState } from "react";
import { Menu } from "../../components/menu/Menu";
import { Search } from "../../components/search/Search";
import { Trending } from "../../components/Trending/Trending";
import { useApi } from "../../hooks/api/api";
import './perfil.css'

export const Perfil = () => {
    const userId = sessionStorage.getItem('user')
    const api = useApi()
    const [user, setUser] = useState()

    useEffect(() => {
        api.getUser(userId).then((response) => {
            setUser(response)
            console.log(response)
        }).catch((err) => {
            console.error(err)
        })
    }, [])

    return (
        <div className="container-fluid home-background">
            <div className="container-fluid home-container">
                <div className="row">
                    <div className="col coluna-1">
                        <Menu />

                    </div>

                    <div className="col-4" >
                        <div className="perfil">
                            <header id="perfil-header">Nome: {user?.username}</header>
                            <section id="perfil-wallpaper"></section>
                            <section id="perfil-photo"></section>
                            <section id="perfil-content">
                                <p>Bio: {user?.bio}</p>
                                <p>Seguidores: {user?.followers.length} &nbsp; Seguindo: {user?.follows.length}</p>
                            </section>
                        </div>
                    </div>
                    <div className="col">
                        <Search />
                        <Trending />
                    </div>
                </div>
            </div>
        </div>
    )
}