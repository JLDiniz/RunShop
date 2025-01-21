import { PercorrerDados } from "./percorrerDados";
import { useEffect, useState } from "react";

export function MainApp() {

    const [database, setDatabase] = useState(
        [
            { 'nome': 'carregando', 'preço': '0' },
        ]
    )

    useEffect(() => {

        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/produtos/listar');
                if (!response.ok) {
                    throw new Error('Erro ao fazer o fetch');
                }
                const result = await response.json();

                setDatabase(result['produtos'])

                console.log(database)
            } catch (error) {
                console.log(error)
            }
        };
    
        fetchData();

    }, []);

    return (
        <div className="principal">
            <div className="divPesquisa">
                <input className="pesquisa" placeholder="Qual item você deseja?" />
                <button className="buttonPesquisa">Pesquisar</button>
            </div>
            <div className="divItem">
                <PercorrerDados array={database}/>
            </div>
        </div>
    );
}
