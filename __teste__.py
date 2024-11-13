from controllers.usuarios import pesquisa_usuario
from controllers.produtos import pesquisa_item
from controllers.geral import conferir_status

resultado_teste_pesquisa_usuario = pesquisa_usuario("dev", "dev")
if(resultado_teste_pesquisa_usuario["status"]):
    print("OK: pesquisa_usuario retorna true para parametros certos.")
else:
    print("Error: pesquisa_usuario")


resultado_teste_pesquisa_usuario = pesquisa_usuario("sadasdasd", "asdasdasd")
if(resultado_teste_pesquisa_usuario["status"]):
    print("ERROR: pesquisa_usuario retorna true para parametros certos.")
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