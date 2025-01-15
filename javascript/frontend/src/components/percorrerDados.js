

export function percorrerDados(array) {
    let contador = 0;
    const result = []
    while (contador < array.length) {

        if (array[contador]['status']) {
            result.push(
                <div className="divteste">
                    <p>Nome: {array[contador]["nome"]}</p>
                    <p>Preço: {array[contador]["preço"]}</p>
                </div>
            )
        }

        contador++;
    }
    return result
}