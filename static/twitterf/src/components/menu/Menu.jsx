import { useNavigate } from "react-router-dom"
import './menu.css'

export const Menu = () => {
    const navigate = useNavigate()

    const toHome = () => {
        navigate('/home')
    }

    const toProfile = () => {
        navigate('/perfil')
    }

    const exit = () => {
        navigate('/')
    }

    return (
        <div className="menu">
            <ol>
                <li onClick={toHome}>
                    <a href=""><i class="fa-brands fa-twitter"></i></a>
                </li>
                <li onClick={toHome}>
                    <a href=""><i class="fa-solid fa-house"></i>&nbsp;Home</a>
                </li>
                <li onClick={toProfile}>
                    <a href=""><i class="fa-solid fa-user"></i> &nbsp;Profile</a>
                </li>
                <li onClick={exit}>
                    <a href=""><i class="fa-solid fa-right-from-bracket"></i> &nbsp;Exit</a>
                </li>
            </ol>
        </div>
    )
}