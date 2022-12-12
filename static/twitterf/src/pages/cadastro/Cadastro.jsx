import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useApi } from "../../hooks/api/api";
import './cadastro.css'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export function Cadastro() {

    const [username, setUserName] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setComfirmPassword] = useState('')
    const [email, setEmail] = useState('')

    const api = useApi()
    const navigate = useNavigate()

    async function handleSignUp(event) {
        event.preventDefault()

        if (password === confirmPassword) {
            const logado = await api.signup(username, password, email)
            if (logado) {
                console.log("aqui")
                toast('🦄 Cadastro feito!', {
                    position: "top-center",
                    autoClose: 5000,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                    theme: "light",
                });
            }
        } else {
            alert("Senhas diferentes!")
        }
    }

    function navLogin() {
        navigate('/')
    }

    return (
        <div className="login-background container-fluid ps-md-0 ">
            <ToastContainer />

            <div className="row g-0">
                <div className="d-none d-md-flex col-md-4 col-lg-6 bg-image"></div>
                <div className="col-md-8 col-lg-6">
                    <div className="login d-flex align-items-center py-5">
                        <div className="container">
                            <div className="row">
                                <div className="col-md-9 col-lg-8 mx-auto">

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
                                            <input value={confirmPassword} onChange={(e) => setComfirmPassword(e.target.value)} type="password" className="form-control" id="floatingPasswordConfirm" placeholder="Confirm Password" />
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
        </div>
    )
}