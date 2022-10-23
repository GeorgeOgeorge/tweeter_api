import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useApi } from "../../hooks/api/api";
import './cadastro.css'

export function Cadastro() {

    const [username, setUserName] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')

    const api = useApi()
    const navigate = useNavigate()

    async function handleSignUp(event) {
        event.preventDefault()

        const logado = await api.signup(username, password, email)
        navigate('/')
    }

    function navLogin() {
        navigate('/login')
    }


    return (
        <div className="container-fluid" style={{backgroundColor: 'black'}}>
            <div className="container">
                <div className="row">
                    <div className="col-md-9 col-lg-8 mx-auto">
                        <div className="card flex-row my-5 border-0 shadow rounded-3 overflow-hidden">
                            <div className="card-img-left d-none d-md-flex">

                            </div>
                            <div className="card-body p-4 p-sm-5">
                                <h5 className="card-title text-center mb-5 fw-light fs-5">Register</h5>
                                <form onSubmit={(e) => handleSignUp(e)}>

                                    <div className="form-floating mb-3">
                                        <input value={username} onChange={(e) => setUserName(e.target.value)} type="text" className="form-control" id="floatingInputUsername" placeholder="myusername" />
                                        <label htmlFor="floatingInputUsername">Username</label>
                                    </div>

                                    <div className="form-floating mb-3">
                                        <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" className="form-control" id="floatingInputEmail" placeholder="name@example.com" />
                                        <label htmlFor="floatingInputEmail">Email address</label>
                                    </div>
                                    <div className="form-floating mb-3">
                                        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" className="form-control" id="floatingPassword" placeholder="Password" />
                                        <label htmlFor="floatingPassword">Password</label>
                                    </div>

                                    <div className="form-floating mb-3">
                                        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" className="form-control" id="floatingPasswordConfirm" placeholder="Confirm Password" />
                                        <label htmlFor="floatingPasswordConfirm">Confirm Password</label>
                                    </div>

                                    <div className="d-grid mb-2">
                                        <button className="btn btn-lg btn-primary btn-login fw-bold text-uppercase" type="submit">Register</button>
                                    </div>

                                    <a onClick={navLogin} className="d-block text-center mt-2 small" href="#">Have an account? Sign In</a>
                                    <hr />
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
    )
}