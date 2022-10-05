import React, { useEffect, useState } from "react";
import { useApi } from "../../hooks/api/api";

export function Home() {
    const api = useApi()
    const userToken = sessionStorage.getItem('user')

    const [posts, setPosts] = useState([])
    const [post, setPost] = useState("")

    useEffect(() => {
        const headers = {
            Authorization: `Token ${userToken}`,
            'content-type': 'application/json',
        };
        api
            .getPost(headers)
            .then((response) => {
                setPosts(response)
            }).catch((err) => {
                console.error(err)
            })
    }, [post])



    function cadastraPost(event) {
        event.preventDefault()
        const headers = {
            Authorization: `Token ${userToken}`,
            'content-type': 'application/json',
        };
        console.log(post)
        api
            .postPost({text: post, location: 'natal'}, headers)
            .then()
            .catch((err) => console.error(err))
    }


    return (
        <div className="container py-5">

            <header className="text-center text-white">
                <h1 className="display-4">TWITTER</h1>
            </header>

            <form onSubmit={(e) => cadastraPost(e)}>
                <div className="mb-3">
                    <label htmlFor="exampleFormControlTextarea1" className="form-label">Post aqui</label>
                    <textarea value={post} onChange={(e) => setPost(e.target.value)} className="form-control" id="exampleFormControlTextarea1" rows={5}></textarea>
                    <button type="submit">Post</button>
                </div>
            </form>


            <div className="row py-5">
                <div className="col-lg-7 mx-auto">

                    {posts.map(post => {
                        return <div key={post.id} className="card shadow mb-4">
                            <div className="card-body p-5">
                                <h4 className="mb-4">Tweet</h4>
                                <p>{post.text}</p>
                                <small>{post.location}</small>
                            </div>
                        </div>
                    })}
                </div>
            </div>
        </div>
    )
}