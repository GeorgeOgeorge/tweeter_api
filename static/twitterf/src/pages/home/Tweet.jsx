import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useApi } from "../../hooks/api/api";
import './home.css';

export function Tweet() {
    const api = useApi()
    const userId = sessionStorage.getItem('user')
    let idObj = useParams()
    const id = Number.parseInt(idObj.id)

    const [posts, setPosts] = useState([])
    const [post, setPost] = useState()
    const [post_id, setPost_id] = useState()
    const [coment, setComent] = useState()
    const [retweets_t, setRetweets_t] = useState([])
    const [retweets_t_ids, setRetweets_t_ids] = useState([])

    useEffect(() => {
        api
            .getRettweets(id)
            .then((response) => {
                setPosts(response)
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
        event.preventDefault()
        api
            .curtePost(postId, userId)
            .then((response) => console.log(response))
            .catch((err) => console.error(err))

        e.target.style.color = 'red'
    }

    function comentaPost(event) {
        event.preventDefault()
        api.
            comentPost(post_id, userId, coment, "natal")
            .then((response) => console.log(response))
            .catch((err) => console.error(err))
    }

    useEffect(() => {
        api
            .getRettweets(id)
            .then((response) => { setRetweets_t_ids([response.retweets]); console.log(retweets_t_ids) })
            .catch((err) => console.error(err))

        // retweets_t_ids.forEach(rt => {
        //     api.getRettweets(rt)
        //         .then((response) => { setRetweets_t(retweets_t, response); console.log(retweets_t) })
        //         .catch((err) => console.error(err))
        // })

    }, [])


    return (
        <div className="container-fluid home-background">
            <div className="container-fluid home-container">
                <div className="row">
                    <div className="col coluna-1">
                        <h4>Tweetter</h4>
                        <ol>
                            <li>Profile</li>
                            <li>Sair</li>
                        </ol>
                    </div>

                    <div className="col-4">

                        <div className="posts">


                            <div key={posts.id} className="card-post">
                                <h5 className="user-post">{posts.tweet_op} <span className="arroba-user">@fulano</span></h5>
                                <small>{posts.location}</small>
                                <div className="card-body p-5">
                                    <p>{posts.text}</p>
                                </div>
                                <i onClick={(e) => curtePost(e, posts.id)} class="fa-solid fa-heart like-heart" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                <i onClick={() => setPost_id(posts.id)} data-bs-toggle="modal" data-bs-target="#exampleModal" class="fa-regular fa-comment" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                            </div>

                            {retweets_t.map(rtt => {
                                <div key={rtt.id} className="card-post">
                                    <h5 className="user-post">{rtt.tweet_op} <span className="arroba-user">@fulano</span></h5>
                                    <small>{rtt.location}</small>
                                    <div className="card-body p-5">
                                        <p>{rtt.text}</p>
                                    </div>
                                    <i onClick={(e) => curtePost(e, rtt.id)} class="fa-solid fa-heart like-heart" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                    <i onClick={() => setPost_id(rtt.id)} data-bs-toggle="modal" data-bs-target="#exampleModal" class="fa-regular fa-comment" style={{ cursor: 'pointer', marginRight: '20px' }}></i>
                                </div>
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
                    <div className="col"></div>
                </div>
            </div>
        </div>
    )
}