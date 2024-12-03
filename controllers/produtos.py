#Esta linha define a função chamada
def carregar_produtos():

    #Aqui, inicializamos uma lista vazia chamada produtos. 
    # Essa lista será usada para armazenar cada produto encontrado no arquivo.
    produtos = []

    #Usamos a instrução with open(...) as file: para abrir um arquivo e garantir que ele será fechado automaticamente ao final. 
    #O segundo argumento, 'r', significa que estamos abrindo o arquivo no modo de leitura.
    with open('C:\\Users\\LUCAS\\OneDrive\\Documentos\\Programação\\RunShop\\controllers\\database_produtos.txt', 'r') as file:
        
        #Aqui, criamos um laço for que percorre cada linha do arquivo. 
        # A cada iteração, a variável linha representa uma linha do arquivo.
        for linha in file:

            #Esta linha remove espaços em branco ou quebras de linha extras do início e fim de linha com o método strip(), 
            #e em seguida divide a linha em partes, usando a vírgula , como separador com split(','). 
            #Isso cria uma lista dados com os elementos separados da linha, como ['1', 'Produto A', '10.50'].
            dados = linha.strip().split(',')

            #Aqui, verificamos se dados tem exatamente 3 elementos (id, nome e preço). 
            # Isso ajuda a garantir que o formato da linha no arquivo esteja correto.
            if len(dados) == 3:

                #Se a linha tiver o formato correto, criamos um dicionário para representar o produto, onde:
                #"id" é o primeiro elemento de dados, convertido para um número inteiro (int(dados[0])).
                #"nome" é o segundo elemento (dados[1]), que representa o nome do produto.
                #"preço" é o terceiro elemento (dados[2]), convertido para um número de ponto flutuante (float(dados[2])).
                #Este dicionário é então adicionado à lista produtos usando o método append().
                produtos.append({
                "id": int(dados[0]),
                "nome": dados[1],
                "preço": float(dados[2])
                })
    #Finalmente, a função retorna a lista produtos, que contém todos os produtos lidos e formatados.
    return produtos

#Esta linha define uma função
def listar_produtos():
    #criando uma variável chamada produtos e atribuindo a ela o resultado da função carregar_produtos()
    produtos = carregar_produtos()
    
    #Este bloco verifica se produtos está vazio (ou seja, se não há produtos cadastrados). 
    #Se produtos for vazio ou None, o if not produtos será verdadeiro, e o código entrará neste bloco. 
    #Então, será exibido um print com um dicionário contendo duas chaves: "status": False: indica que a operação 
    # não foi bem-sucedida (não há produtos).
    #"mensagem": "Nenhum produto cadastrado.": uma mensagem informando que não há produtos cadastrados.
    if not produtos:
        print({
            "status": False,
            "mensagem": "Nenhum produto cadastrado."
        }) 
    
    #Este é um laço for que itera sobre cada produto em produtos. 
    # Para cada produto (item), o código exibe o id, o nome e o preço do produto, acessando cada campo pelo nome da chave
    for item in produtos:
        print(item['id'], item['nome'], item['preço'])


#Aqui estamos definindo uma função chamada pesquisa_item. 
# Ela recebe um argumento, nome_item, que representa o nome do produto que queremos procurar na lista de produtos.
def pesquisa_item(nome_item):

    #qui, estamos chamando uma função chamada carregar_produtos() para obter uma lista de produtos. 
    # O resultado é armazenado na variável database_produtos.
    database_produtos = carregar_produtos()
    
    #Aqui iniciamos um laço for que percorre cada item em database_produtos. 
    # Cada item é armazenado na variável produto enquanto o laço passa por todos os produtos.
    for produto in database_produtos:

        #Esta linha verifica se o valor da chave "nome" dentro do dicionário produto é igual ao nome_item fornecido na função. 
        # Se forem iguais, significa que encontramos o produto procurado.
        if produto["nome"] == nome_item:

            #Se o produto for encontrado, a função imediatamente retorna um dicionário com três chaves:
            return {
                "status": True,
                "item": produto,
                "mensagem": "Produto encontrado!"
            }

    #Se o laço for terminar e nenhum produto for encontrado, a função retorna um dicionário indicando que o produto não foi encontrado.        
    return {
        "status": False,
        "item": {},
        "mensagem": "Item não encontrado"
    }


def cadastrar_produto(nome, preco):
    # Carregar produtos atuais
    produtos = carregar_produtos()
    
    # Obter o último ID e incrementar
    ultimo_produto_id = produtos[-1]["id"] if produtos else 0
    novo_produto_id = ultimo_produto_id + 1

    # Adicionar novo produto
    novo_produto = {"id": novo_produto_id, "nome": nome, "preço": preco}

    # Salvar o novo produto no final do arquivo sem apagar os anteriores
    with open('C:\\Users\\LUCAS\\OneDrive\\Documentos\\Programação\\RunShop\\controllers\\database_produtos.txt', 'a') as file:
        # Adiciona uma nova linha para separar do último registro, caso o arquivo não esteja vazio
        if produtos:
            file.write("\n")
        file.write(f"{novo_produto['id']},{novo_produto['nome']},{novo_produto['preço']}")

    return {
        "status": True,
        "mensagem": "Produto cadastrado com sucesso!",
        "produto": novo_produto
    }

def deletar_produto(produto_id):
    # Carregar produtos atuais
    produtos = carregar_produtos()
    
    # Encontrar o produto a ser deletado
    produto_a_deletar = next((produto for produto in produtos if produto["id"] == produto_id), None)
    
    if not produto_a_deletar:
        return {
            "status": False,
            "mensagem": "Produto não encontrado."
        }
    
    # Remover o produto da lista
    produtos = [produto for produto in produtos if produto["id"] != produto_id]
    
    # Salvar a lista atualizada no arquivo
    with open('C:\\Users\\LUCAS\\OneDrive\\Documentos\\Programação\\RunShop\\controllers\\database_produtos.txt', 'w') as file:
        for i, produto in enumerate(produtos):
            if i > 0:
                file.write("\n")
            file.write(f"{produto['id']},{produto['nome']},{produto['preço']}")
    
    return {
        "status": True,
        "mensagem": "Produto deletado com sucesso!",
        "produto": produto_a_deletar
    }


def check_id_produtos (id):
    produtos = carregar_produtos()

    for item in produtos:
        if item['id'] == id:
            return {
                'status': True,
                'mensagem': 'O item com esse id esta cadastrado.'
            }

    return {
            'status': False,
            'mensagem': 'O item com esse id não esta cadastrado.'
        }
    