import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Menu } from "../../components/menu/Menu";
import { Search } from "../../components/search/Search";
import { Trending } from "../../components/Trending/Trending";
import { useApi } from "../../hooks/api/api";
import './home.css';

export function Home() {
    const api = useApi()
    const userId = sessionStorage.getItem('user')
    const navigate = useNavigate()

    const [posts, setPosts] = useState([])
    const [post, setPost] = useState()
    const [post_id, setPost_id] = useState()
    const [coment, setComent] = useState()
    const [retweets_t, setRetweets_t] = useState([])

    useEffect(() => {
        api
            .getPost()
            .then((response) => {
                setPosts(response)
                console.log(response)
            }).catch((err) => {
                console.error(err)
            })
    }, [post])

    function cadastraPost(event) {
        event.preventDefault()
        api
            .postPost({ text: post, location: 'natal', user_id: userId })
            .then()
            .catch((err) => console.error(err))

        setPost('')
    }

    function curtePost(event, postId) {
        console.log(post_id)

        event.preventDefault()
        api
            .curtePost(postId, userId)
            .then((response) => console.log(response))
            .catch((err) => console.error(err))

        event.target.style.color = 'red'
    }

    function comentaPost(event) {
        console.log(post_id)
        event.preventDefault()
        api.
            comentPost(post_id, userId, coment, "natal")
            .then((response) => console.log(response))
            .catch((err) => console.error(err))
    }

    function getRettweets(e, id) {
        e.preventDefault()
        navigate(`/tweet/${id}`)
    }

    function toProfile(id) {
        navigate(`/perfil/${id}`)
    }


    return (
        <div className="container-fluid home-background">
            <div className="container-fluid home-container">
                <div className="row">
                    <div className="col coluna-1">
                        <Menu />

                    </div>

                    <div className="col-4" >
                        <form id="form-post" onSubmit={(e) => cadastraPost(e)}>
                            <div className="mb-3">
                                <label htmlFor="exampleFormControlTextarea1" className="form-label home-post">Home</label>
                                <textarea value={post} onChange={(e) => setPost(e.target.value)}
                                    className="form-control input-post" id="exampleFormControlTextarea1" rows={5} placeholder="O que há de novo?" />
                                <div className="buttons">
                                    <button className="button-post" type="submit">Tweet</button>
                                </div>

                            </div>
                        </form>

                        <div className="posts">
                            {posts.map((post) => {
                                return (
                                    <div key={post.id} className="card-post" >
                                        <h5 className="user-post" onClick={() => toProfile(post.tweet_op.id)} style={{ cursor: 'pointer' }}>{post.tweet_op.username} </h5>
                                        <small>{post.location}</small>
                                        <div className="card-body p-5" onClick={(e) => getRettweets(e, post.id)} style={{ cursor: 'pointer' }} >
                                            <p>{post.text}</p>
                                        </div>
                                        <i onClick={(e) => curtePost(e, post.id)} class="fa-solid fa-heart like-heart" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                        <i onClick={() => setPost_id(post.id)} data-bs-toggle="modal" data-bs-target="#exampleModal" class="fa-regular fa-comment" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                    </div>
                                )
                            })}

                        </div>

                        {/* <!-- Modal --> */}
                        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Coment algo</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <textarea value={coment} onChange={(e) => setComent(e.target.value)}
                                            className="form-control input-post" id="exampleFormControlTextarea1" rows={5} placeholder="O que há de novo?" />
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                                        <button onClick={comentaPost} type="button" class="btn btn-primary">Comentar</button>
                                    </div>
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
    )
}