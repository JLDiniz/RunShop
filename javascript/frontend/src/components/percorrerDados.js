

export function PercorrerDados({ array }) {
    let contador = 0;
    const result = [];

    while (contador < array.length) {

        result.push(
            <div className="divteste" key={contador}>
                <p>Nome: {array[contador]["nome"]}</p>
                <p>Preço: {array[contador]["preço"]}</p>
            </div>
        );

        contador++;
    }

    return result;
};