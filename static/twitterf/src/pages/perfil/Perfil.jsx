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
    const [posts, setPosts] = useState([])


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

    function editProfile(event) {
        event.preventDefault();
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

    useEffect(() => {
        api
            .getPostsUser(user_current_id)
            .then((response) => {
                setPosts(response)
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

                    <div className="col-4">
                        <div className="perfil">
                            <header id="perfil-header"> <strong>{user?.username}</strong> </header>
                            <section id="perfil-wallpaper"></section>
                            <section id="perfil-photo"></section>
                            <section id="perfil-content">
                                <p>{user?.bio}</p>
                                <p>
                                    Followers: {user?.followers.length} &nbsp; Following:{" "}
                                    {user?.follows.length}
                                </p>
                                {user?.id !== Number.parseInt(userIdLogado) ? (
                                    user?.followers.id === Number.parseInt(userIdLogado) ? (
                                        <button className="btn btn-info"
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
                                        <button className="btn btn-info"
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
                                <button className="btn btn-info" data-bs-toggle="modal" data-bs-target="#exampleModal">Editar Perfil</button>

                            </section>
                        </div>
                        <div className="posts">
                            {posts.map((post) => {
                                return (
                                    <div key={post.id} className="card-post" >
                                        <h5 className="user-post" onClick={() => toProfile(post.tweet_op.id)} style={{ cursor: 'pointer' }}>{post.tweet_op.username} </h5>
                                        <small> <strong>From</strong>  {post.location}</small>
                                        <div className="user-tweet" onClick={(e) => getRettweets(e, post.id)} style={{ cursor: 'pointer' }} >
                                            <p>{post.text}</p>
                                        </div>
                                        <i onClick={(e) => curtePost(e, post.id)} class="fa-solid fa-heart like-heart" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                        <i onClick={() => preComentaPost(post.id, post)} data-bs-toggle="modal" data-bs-target="#exampleModal" class="fa-regular fa-comment" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                    </div>
                                )
                            })}

                        </div>
                    </div>
                    <div style={{ color: 'black' }} class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <form class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Edit Profile</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">@</span>
                                    <input required value={username} onChange={(e) => setUsername(e.target.value)} type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" />
                                </div>

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Password</span>
                                    <input required value={password} onChange={(e) => setPassword(e.target.value)} type="password" class="form-control" placeholder="****" aria-label="Username" aria-describedby="basic-addon1" />
                                </div>

                                <div class="input-group mb-3">
                                    <input value={email} onChange={(e) => setEmail(e.target.value)} type="text" class="form-control" placeholder="Email" aria-label="Recipient's username" aria-describedby="basic-addon2" />
                                    <span class="input-group-text" id="basic-addon2">@example.com</span>
                                </div>

                                <div class="input-group mb-3">
                                    <span class="input-group-text">Bio</span>
                                    <textarea value={bio} onChange={(e) => setBio(e.target.value)} class="form-control" aria-label="With textarea"></textarea>
                                </div>

                                <div class="input-group mb-3">
                                    <span class="input-group-text">Location</span>
                                    <input value={location} onChange={(e) => setLocation(e.target.value)} type="text" class="form-control" aria-label="Amount (to the nearest dollar)" />
                                    <span class="input-group-text">City - State</span>
                                </div>

                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                                    <button type="button" onClick={editProfile} class="btn btn-primary">Editar</button>
                                </div>
                            </div>
                        </form>
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
