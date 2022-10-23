import React, { useEffect, useState } from "react";
import { useApi } from "../../hooks/api/api";
import './home.css';

export function Home() {
    const api = useApi()
    const userId = sessionStorage.getItem('user')

    const [posts, setPosts] = useState([])
    const [post, setPost] = useState()

    useEffect(() => {
        api
            .getPost()
            .then((response) => {
                setPosts(response)
            }).catch((err) => {
                console.error(err)
            })
    }, [post])

    function cadastraPost(event) {
        event.preventDefault()
        const headers = {
                    Authorization: `Bearer ${userToken}`,
                    'content-type': 'application/json',
                };
        api
            .postPost({ text: post, location: 'natal', user_id: userId })
            .then()
            .catch((err) => console.error(err))

        setRefresh(refresh + 1)
        setPost('')
    }

    function curtePost(e, postId) {
        event.preventDefault()
        console.log(postId, userId)
        api
            .curtePost(postId, userId)
            .then((response) => console.log(response))
            .catch((err) => console.error(err))

        e.target.style.color = 'red'
    }


    return (
        <div className="container-fluid home-background">
            <div className="container">

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

                    {posts.map(post => {
                        return <div key={post.id} className="card-post">
                                    <h5 className="user-post">{post.tweet_op} <span className="arroba-user">@fulano</span></h5>
                                    <small>{post.location}</small>
                                    <div className="card-body p-5">
                                        <p>{post.text}</p>
                                    </div>
                                    <i onClick={(e) => curtePost(e, post.id)} class="fa-solid fa-heart like-heart" style={{cursor: 'pointer'}}></i>
                                </div>
                    })}
                </div>
            </div>
        </div>
    )
}