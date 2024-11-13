def conferir_status (param):

    print('Conferindo...')

    if param["status"]:
        # Aqui ele exec se true

        if param["mensagem"]:# Aqui ele exec se o parametro tiver mensagem
            print(param["mensagem"])

        else:# Aqui ele exec se o parametro nao tiver mensagem
            print('O resultado é positivo, mas o parametro nao tem mensagem!')

        return {
            "status": True
        }

    else:
        # Aqui ele exec se status false

        if param["mensagem"]:# Aqui ele exec se o parametro tiver mensagem
            print(param["mensagem"])

        else:# Aqui ele exec se o parametro nao tiver mensagem
            print('O resultado é negativo e o parametro nao tem mensagem!')
        
        return {
            "status": False
        }
