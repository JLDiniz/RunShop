import {percorrerDados} from "@/components/percorrerDados"

const database = [
    { 'nome': 'tenis', 'preço': '27', 'status': true },
    { 'nome': 'damasco', 'preço': '29', 'status': true },
    { 'nome': 'madelei', 'preço': '25', 'status': true },
    { 'nome': 'banana', 'preço': '22', 'status': true },
    { 'nome': 'canela', 'preço': '22', 'status': true }
]


export function MainApp() {
    return (
        <div className="principal">
            <div className="divPesquisa">
                <input className="pesquisa" placeholder="Qual item você deseja?"></input>
                <button className="buttonPesquisa">Pesquisar</button>
            </div>
            <div className="divItem">
                {percorrerDados(database)}
            </div>
        </div>
    )
}