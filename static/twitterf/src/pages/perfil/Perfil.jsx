import { useEffect } from "react";
import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Menu } from "../../components/menu/Menu";
import { Search } from "../../components/search/Search";
import { Trending } from "../../components/Trending/Trending";
import { useApi } from "../../hooks/api/api";
import "./perfil.css";

export const Perfil = () => {
    const userIdLogado = sessionStorage.getItem("user");
    const { id } = useParams();
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [bio, setBio] = useState('');
    const [email, setEmail] = useState('');
    const [location, setLocation] = useState('');

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

    function block(data) {
        api.block(data)
    }

    function editProfile() {
        api.editProfile(user_current_id, {
            username: username,
            password: password,
            bio: bio,
            email: email,
            location: location,
            website: "",
            phone: "",
            birth_date: null,
            date_joined: ""
        })
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
                                {user?.id !== Number.parseInt(userIdLogado) ? (
                                    user?.blocks.id === Number.parseInt(userIdLogado) ? (
                                        <button onClick={() => block({
                                            user_pk: Number.parseInt(userIdLogado),
                                            follow_pk: user.id,
                                        })}>Desbloquear</button>
                                    ) : (
                                        <button onClick={() => block({
                                            user_pk: Number.parseInt(userIdLogado),
                                            follow_pk: user.id,
                                        })}>Bloquear</button>
                                    )
                                ) : null}
                                <button data-bs-toggle="modal" data-bs-target="#exampleModal">Editar Perfil</button>

                            </section>
                        </div>
                    </div>
                    <div style={{ color: 'black' }} class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Edite seu perfil</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <label htmlFor="username">username</label> <br />
                                    <input value={username} onChange={(e) => setUsername(e.target.value)} type="text" name="username" id="" />
                                </div>
                                <div class="modal-body">
                                    <label htmlFor="username">password</label><br />
                                    <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" name="username" id="" />
                                </div>
                                <div class="modal-body">
                                    <label htmlFor="username">bio</label><br />
                                    <textarea value={bio} onChange={(e) => setBio(e.target.value)} name="" id="" cols="30" rows="5"></textarea>
                                </div>
                                <div class="modal-body">
                                    <label htmlFor="username">email</label><br />
                                    <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" name="username" id="" />
                                </div>
                                <div class="modal-body">
                                    <label htmlFor="username">location</label><br />
                                    <input value={location} onChange={(e) => setLocation(e.target.value)} type="text" name="username" id="" />
                                </div>

                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                                    <button onClick={editProfile} type="button" class="btn btn-primary">Editar</button>
                                </div>
                            </div>
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
