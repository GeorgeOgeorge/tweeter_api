import { Menu } from "../../components/menu/Menu";
import { Search } from "../../components/search/Search";
import { Trending } from "../../components/Trending/Trending";

export const Perfil = () => {
    return (
        <div className="container-fluid home-background">
            <div className="container-fluid home-container">
                <div className="row">
                    <div className="col coluna-1">
                        <Menu />

                    </div>

                    <div className="col-4" >
                        <div className="perfil">
                            <header id="perfil-header"></header>
                            <section id="perfil-wallpaper"></section>
                            <section id="perfil-photo"></section>
                            <section id="perfil-content"></section>
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