
#Aqui, estamos definindo uma função chamada carregar_usuarios. 
# Essa função não recebe parâmetros e tem o objetivo de carregar uma lista de usuários a partir de um arquivo.
def carregar_usuarios():

    #Aqui, criamos uma lista vazia chamada usuarios, onde vamos armazenar cada usuário (como um dicionário) lido do arquivo.
    usuarios = []

  # Esta linha abre o arquivo localizado no caminho especificado. O modo 'r' indica que estamos abrindo o arquivo apenas para leitura. 
  # O with garante que o arquivo será fechado automaticamente após sua leitura.
    with open('C:\\Users\\jluca\\OneDrive\\Área de Trabalho\\Programação\\RunShop\\controllers\\database_usuario.txt', 'r') as file:

        # Aqui lemos a primeira linha do arquivo e armazenamos o conteúdo na variável linha. Cada linha deve conter dados de um usuário.
        linha = file.readline()  

        #Este while cria um loop que continuará enquanto linha tiver algum conteúdo, ou seja, enquanto não chegarmos ao fim do arquivo.
        while linha:  
            
            #Aqui, estamos processando o conteúdo de linha:
            #linha.strip() remove qualquer espaço em branco (incluindo quebras de linha) no início e no final da linha.
            #.split(',') divide a linha em uma lista de itens (dados) separados por vírgula. 
            # Assim, dados conterá uma lista com as partes individuais (nome, email e senha).
            dados = linha.strip().split(',')

            # Aqui verificamos se dados tem exatamente 3 itens, que são o nome, email e senha do usuário. 
            # Isso ajuda a garantir que estamos lidando com uma linha bem formatada.
            if len(dados) == 3:  
                usuarios.append({
                    "nome": dados[0],
                    "email": dados[1],
                    "senha": dados[2]
                })
            linha = file.readline()  # Ler a próxima linha

    # No final a function retorna a array (lista) de usuarios.
    return usuarios

def validar_login(email, senha):
    database_usuarios = carregar_usuarios()  # Carregar usuários do arquivo
    
    contador = 0
    while contador < len(database_usuarios):
        if database_usuarios[contador]["email"] == email:
            if database_usuarios[contador]["senha"] == senha:
                return {
                    "status": True,
                    "conta": database_usuarios[contador],
                    "mensagem": "Conta encontrada!"               
                }
        contador += 1

    return {
        "status": False,
        "conta": {},
        "mensagem": "Conta não encontrada"
    }
