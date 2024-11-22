from controllers.pesquisa_usuario import pesquisa_usuario
from controllers.produtos import pesquisa_item, carregar_produtos, cadastrar_produto
from controllers.geral import conferir_status

resultado_teste_pesquisa_usuario = pesquisa_usuario("dev")
if(resultado_teste_pesquisa_usuario["status"]):
    print("OK: pesquisa_usuario retorna true para parametros certos.")
else:
    print("Error: pesquisa_usuario")


resultado_teste_pesquisa_usuario = pesquisa_usuario("sadasdasd")
if(resultado_teste_pesquisa_usuario["status"]):
    print("ERROR: pesquisa_usuario retorna true para parametros errados.")
else:
    print("OK: pesquisa_usuario retorna false para parametros certos.")


resultado_teste_pesquisa_item = pesquisa_item("tenis")
if(resultado_teste_pesquisa_item["status"]):
     print("OK: pesquisa_item retornou a mensagem esperada.")
else:
    print("Error: pesquisa_item")


resultado_teste_pesquisa_item = pesquisa_item("pulseira")
if(resultado_teste_pesquisa_item["status"]):
    print("Error: pesquisa_item")
else:
    print("OK: pesquisa_item retornou a mensagem esperada.")


exemplo_teste_conferir_status = {
                                    "status": True,
                                    "conta": {},
                                    "mensagem": "conta encontrada! Seja Bem-Vindo!"               
                                    }

resultado_teste_conferir_status = conferir_status(exemplo_teste_conferir_status)
if(resultado_teste_conferir_status["status"]):
     print("OK: conferir_status retornou a mensagem esperada para True.")
else:
    print("Error: conferir_status")


exemplo_teste_conferir_status = {
                                    "status": False,
                                    "conta": {},
                                    "mensagem": "conta não encontrada"
                                    }

resultado_teste_conferir_status = conferir_status(exemplo_teste_conferir_status)
if(resultado_teste_conferir_status["status"]):
    print("Error: conferir_status")
else:
    print("OK: conferir status retornou a mensagem esperada para False")


# Teste carregar produtos
resultado_teste_carregar_produto = carregar_produtos()
if isinstance(resultado_teste_carregar_produto, list) == True:
    if isinstance(resultado_teste_carregar_produto[0]["id"], int) and isinstance(resultado_teste_carregar_produto[0]["nome"], str) and isinstance(resultado_teste_carregar_produto[0]["preço"], float):
        print("Ok: carregar_produtos")
else:
    print('Error: carregar produto, carregar produto nao retornou uma lista.')

# Teste para cadastrar produto
def carregar_produtos_mock(): # Simulando a função carregar_produtos para diferentes cenários
    return [
        {'id': 1, 'nome': 'Caderno', 'preço': 12.5},
        {'id': 2, 'nome': 'Caneta', 'preço': 1.99}
    ]  # Produtos simulados

# Testes positivos
def teste_cadastrar_produto_positivo():
    global carregar_produtos  # Substituímos a função original por uma simulação
    carregar_produtos = carregar_produtos_mock
    
    # Simulando o cadastro de um novo produto
    resultado = cadastrar_produto("camelback", 15.2)
    print("Teste Positivo 1:", "Passou" if resultado["status"] and resultado["produto"]["nome"] == "camelback" else "Falhou")
    
# Testes negativos
def teste_cadastrar_produto_negativo():
    global carregar_produtos
    carregar_produtos = carregar_produtos_mock
    
    # Tentando cadastrar um produto sem nome
    try:
        resultado = cadastrar_produto("", 1.99)
        print("Teste Negativo 1:", "Falhou" if resultado["status"] else "Passou")
    except Exception as e:
        print("Teste Negativo 1: Passou (Erro esperado)", e)
    
    # Tentando cadastrar um produto com preço inválido
    try:
        resultado = cadastrar_produto("Régua", -5)
        print("Teste Negativo 2:", "Falhou" if resultado["status"] else "Passou")
    except Exception as e:
        print("Teste Negativo 2: Passou (Erro esperado)", e)

# Executando os testes
teste_cadastrar_produto_positivo()
teste_cadastrar_produto_negativo()


