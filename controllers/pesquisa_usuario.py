def carregar_usuarios():
    usuarios = []
    """
        Com o "with" voce consegue abrir algo, como um arquivo por exemplo, e com o "as", voce coloca ele em uma variavel, por exemplo, "as file" = "como file"
        onde "file" vai ser a variavel do arquivo. Podendo assim ler e escrever no "file".
        Use "r" para read (ler), e "w" para write (escrever).
    """
    with open('C:\\Users\\jluca\\OneDrive\\Área de Trabalho\\Programação\\backend\\aula-1\\homework\\pesquisas\\controllers\\database_usuario.txt', 'r') as file:

        linha = file.readline()  # Ler a primeira linha

        while linha:  # Enquanto houver linhas no arquivo
            
            # separa os dados ("objetos", palavras), por ",".
            dados = linha.strip().split(',')

            if len(dados) == 3:  # Apenas usuários têm 3 campos, ou seja, aqui ele confere se voce esta passando 3 dados para ele ler (nome, email e senha).
                usuarios.append({
                    "nome": dados[0],
                    "email": dados[1],
                    "senha": dados[2]
                })
            linha = file.readline()  # Ler a próxima linha

    # No final a function retorna a array (lista) de usuarios.
    return usuarios

def listar_usuarios():
    # Carregar usuários atuais
    usuarios = carregar_usuarios()
    
    # Verificar se a lista de usuários está vazia
    if not usuarios:
        print({
            "status": False,
            "mensagem": "Nenhum usuário cadastrado."
        })
        return  # Interrompe a função se não houver usuários

    # Exibir cada usuário (omitindo a senha por segurança)
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")

def check_nome_usuario(nome):
    # Carregar lista de usuários atual
    usuarios = carregar_usuarios()

    # Verificar se o nome do usuário existe na lista
    for usuario in usuarios:
        if usuario['nome'] == nome:
            return {
                'status': True,
                'mensagem': 'O usuário com esse nome já está cadastrado.'
            }

    return {
        'status': False,
        'mensagem': 'O usuário com esse nome não está cadastrado.'
    }


def pesquisa_usuario(email):
    database_usuarios = carregar_usuarios()
    
    contador = 0
    while contador < len(database_usuarios):
        if database_usuarios[contador]["email"] == email:
            return {
                "status": True,
                "conta": database_usuarios[contador],
                "mensagem": "conta encontrada!"
            }
        contador += 1
    
    return {
        "status": False,
        "conta": {},
        "mensagem": "conta não encontrada"
    }

def cadastrar_usuario(nome, email, senha):
    # Carregar usuários atuais
    usuarios = carregar_usuarios()
    
    # Verificar se o e-mail já existe
    contador = 0
    while contador < len(usuarios):
        if usuarios[contador]["email"] == email:
            return {
                "status": False,
                "mensagem": "E-mail já cadastrado!"
            }
        contador += 1

    # Adicionar novo usuário
    usuarios.append({"nome": nome, "email": email, "senha": senha})

    # Salvar usuários de volta no arquivo
    with open('C:\\Users\\jluca\\OneDrive\\Área de Trabalho\\Programação\\backend\\aula-1\\homework\\pesquisas\\controllers\\database_usuario.txt', 'w') as file:
        contador = 0
        while contador < len(usuarios):
            usuario = usuarios[contador]
            file.write(f"{usuario['nome']},{usuario['email']},{usuario['senha']}\n")
            contador += 1

    return {
        "status": True,
        "mensagem": "Usuário cadastrado com sucesso!"
    }

def deletar_usuario(nome):
    # Carregar lista de usuários atual
    usuarios = carregar_usuarios()
    
    # Encontrar o usuário a ser deletado usando apenas o nome
    usuario_a_deletar = next((usuario for usuario in usuarios if usuario["nome"] == nome), None)
    
    # Verificar se o usuário foi encontrado
    if not usuario_a_deletar:
        return {
            "status": False,
            "mensagem": "Usuário não encontrado."
        }
    
    # Remover o usuário da lista com base no nome
    usuarios = [usuario for usuario in usuarios if usuario["nome"] != nome]
    
    # Salvar a lista atualizada no arquivo
    try:
        with open('C:\\Users\\jluca\\OneDrive\\Área de Trabalho\\Programação\\backend\\aula-1\\homework\\pesquisas\\controllers\\database_usuario.txt', 'w') as file:
            for i, usuario in enumerate(usuarios):
                if i > 0:
                    file.write("\n")
                file.write(f"{usuario['nome']},{usuario['email']},{usuario['senha']}")
    
    except Exception as e:
        return {
            "status": False,
            "mensagem": f"Erro ao salvar a database: {e}"
        }
    
    return {
        "status": True,
        "mensagem": "Usuário deletado com sucesso!",
        "usuario": usuario_a_deletar
    }
