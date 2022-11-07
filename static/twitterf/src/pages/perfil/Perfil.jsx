import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";
import { Menu } from "../../components/menu/Menu";
import { Search } from "../../components/search/Search";
import { Trending } from "../../components/Trending/Trending";
import { useApi } from "../../hooks/api/api";
import "./perfil.css";

export const Perfil = () => {
    const userIdLogado = sessionStorage.getItem("user");
    const { id } = useParams();

    const user_current_id = id
        ? Number.parseInt(id)
        : Number.parseInt(userIdLogado);

    const api = useApi();
    const [user, setUser] = useState();

    useEffect(() => {
        api
            .getUser(user_current_id)
            .then((response) => {
                setUser(response);
                console.log(response);
            })
            .catch((err) => {
                console.error(err);
            });
    }, []);

    function follow(data) {
        api.follow(data);
    }

    function block() {

    }

    return (
        <div className="container-fluid home-background">
            <div className="container-fluid home-container">
                <div className="row">
                    <div className="col coluna-1">
                        <Menu />
                    </div>

                    <div className="col-4">
                        <div className="perfil">
                            <header id="perfil-header">Nome: {user?.username}</header>
                            <section id="perfil-wallpaper"></section>
                            <section id="perfil-photo"></section>
                            <section id="perfil-content">
                                <p>Bio: {user?.bio}</p>
                                <p>
                                    Seguidores: {user?.followers.length} &nbsp; Seguindo:{" "}
                                    {user?.follows.length}
                                </p>
                                {user?.id !== Number.parseInt(userIdLogado) ? (
                                    user?.followers.id === Number.parseInt(userIdLogado) ? (
                                        <button
                                            onClick={() =>
                                                follow({
                                                    user_pk: Number.parseInt(userIdLogado),
                                                    follow_pk: user.id,
                                                })
                                            }
                                        >
                                            Deixar de seguir
                                        </button>
                                    ) : (
                                        <button
                                            onClick={() =>
                                                follow({
                                                    user_pk: Number.parseInt(userIdLogado),
                                                    follow_pk: user.id,
                                                })
                                            }
                                        >
                                            Seguir
                                        </button>
                                    )
                                ) : null}
                                <button onClick={block}>Bloquear</button>
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
    );
};
