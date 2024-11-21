
from controllers.usuarios import validar_login
from controllers.geral import conferir_status
from controllers.produtos import pesquisa_item, cadastrar_produto, listar_produtos, deletar_produto, check_id_produtos
from controllers.pesquisa_usuario import pesquisa_usuario, cadastrar_usuario, listar_usuarios, check_nome_usuario, deletar_usuario


aplicacao_online = True

while aplicacao_online == True:
    # Precisamos receber uma variavel com um input, sendo ela a variavel de 1 ou 2, sendo 1 controle de usuario ou 2 controle de produto.
    tipo_login = int(input("Selecione 1 para logar no controle de usuários ou 2 para controle de produtos: "))
    # Fazer uma condição para verivicar se essa variavel vai receber a opção para ir para controle de usuario ou produto
    if (tipo_login == 1): #usuario
        contador_tentativas_login_usuario = 0

        while contador_tentativas_login_usuario < 3:

            resultado_email = input("Digite o email: ")
            resultado_senha = input("Digite sua senha: ")
            
            resultado_pesquisa_usuario = validar_login(resultado_email, resultado_senha)

            resultado_conferir_status = conferir_status(resultado_pesquisa_usuario)

            if (resultado_conferir_status["status"]):
                sair_pesquisa = False
                sair_menu_opçoes = False
                while sair_menu_opçoes == False:
                    menu_opcao = int(input("Seja bem vindo! Digite 10 para encerrar a aplicação, 0 para deslogar, 1 para pesquisar o usuário, 2 para cadastrar, 3 para listar ou 4 para deletar: "))
                    
                    if (menu_opcao == 10): # encerrar
                        print(menu_opcao)
                        aplicacao_online = False
                        sair_pesquisa = True
                        contador_tentativas_login_usuario = 3

                    if (menu_opcao == 0): # deslogar
                        sair_pesquisa = True
                        
                    if (menu_opcao == 1): # pesquisar
                        sair_pesquisa = False
                        while sair_pesquisa == False :
                            resultado_pesquisa_input = input("Qual conta você deseja? ")
                            
                            if (resultado_pesquisa_input == 0):
                                sair_pesquisa = True
                                
                            # Só entra nesse else se resultado_pesquisa_input for diferente de '0'
                            else:
                                resultado_pesquisa_usuario = pesquisa_usuario(resultado_pesquisa_input)

                                resultado_conferir_status_usuario = conferir_status(resultado_pesquisa_usuario)
                                if (resultado_conferir_status_usuario["status"]):
                                    print("Nome: ", resultado_pesquisa_usuario["conta"]["nome"])

                    if (menu_opcao == 2): # cadastrar
                        nome = input("Digite o nome: ")
                        email = input("Digite o email: ")
                        senha = input("Digite a senha: ")

                        resultado_cadastro_usuario = cadastrar_usuario(nome, email, senha)

                        if (resultado_cadastro_usuario["status"]):
                            print(resultado_cadastro_usuario["mensagem"])
                        else:
                            print('Erro ao cadastrar produto')
                    
                    if(menu_opcao == 3): #listar
                        listar_usuarios()

                    if(menu_opcao == 4): #deletar
                        usuario_a_deletar = input("Digite o nome do usuário que deseja deletar: ")
                        
                        status_nome_database = check_nome_usuario(usuario_a_deletar)
                        
                        if status_nome_database['status']:
                            print(status_nome_database["mensagem"])
                            confirmação = int(input("Tem certeza que deseja apagar? Digite 0 para SIM ou 1 para cancelar a operação."))
                            
                            if confirmação == 0:
                                resultado_deletar_usuario = deletar_usuario(usuario_a_deletar)
                                print(resultado_deletar_usuario['mensagem'])


                            if confirmação == 1:
                                print('Operação cancelada')

                        else:
                            print(status_nome_database["status"])

            else:
                contador_tentativas_login_usuario += 1

    if (tipo_login == 2): #produto
    # Se produto
        # Que as perguntas de usuario seja feitas 3 vezes, caso ele nao acerte as credenciais.
        contador_tentativas_login = 0
        # enquanto nao acerte, repita.
        while contador_tentativas_login < 3:
                
            # no maximo 3 vezes.
            #Solicita o usuário email e senha
            resultado_email = input("Digite o email: ")
            resultado_senha = input("Digite sua senha: ")

            #Resultado_pesquisa_usuario recebe a função pesquisa usuario com os inputs de email e senha
            resultado_pesquisa_usuario = validar_login(resultado_email, resultado_senha)

            #Resultado_conferir_status recebe a função conferir_status com o resultado da pesquisa_usuario e retorna o status
            resultado_conferir_status = conferir_status(resultado_pesquisa_usuario)

            #Se status for verdadeiro solicita o item ao usuário
            if(resultado_conferir_status["status"]):
                sair_menu_opçoes = False
                while sair_menu_opçoes == False:
                    menu_opcao = int(input('Seja bem vindo! Digite 10 para encerrar a aplicação, 0 para deslogar, 1 para pesquisar o produto, 2 para cadastrar, 3 para listar ou 4 para deletar: '))

                    if (menu_opcao == 10):
                        print(menu_opcao)
                        aplicacao_online = False
                        sair_menu_opçoes = True
                        contador_tentativas_login = 3
                    
                    if(menu_opcao == 0):
                        sair_menu_opçoes = True
                        print(sair_menu_opçoes)
                        
                    if(menu_opcao == 1):
                        sair_pesquisa = False
                        while sair_pesquisa == False :

                            #Resultado_pesquisa_item recebe o item que o usuario deseja
                            resultado_pesquisa_input = input("Qual item você deseja? ")
                            
                            if ( resultado_pesquisa_input == 'Fechar' or resultado_pesquisa_input == 'fechar'):
                                sair_pesquisa = True
                                contador_tentativas_login = 0
                                
                            else:
                                #Resultado_pesquisa_item recebe a função pesquisa_item com o resultado do item solicitado pelo usuario
                                resultado_pesquisa_item = pesquisa_item(resultado_pesquisa_input)
                                
                                #Resultado_conferir_status_item recebe a função conferir_status com o resultado_pesquisa_item
                                resultado_conferir_status_item = conferir_status(resultado_pesquisa_item)

                                if ( resultado_conferir_status_item["status"]):
                                    print("Item:", resultado_pesquisa_item["item"]["nome"])
                                    print("R$", resultado_pesquisa_item["item"]["preço"])

                    if(menu_opcao == 2):

                        sair_cadastro = False
                        while sair_cadastro == False:

                            print('Digite "cancelar" para sair do cadastro de produtos.')

                            nome = input("Digite o nome: ")

                            if (nome == 'cancelar' or nome == 'Cancelar'):
                                sair_cadastro = True
                                sair_pesquisa = True

                            else:
                                preço = int(input("Digite o preço: "))
                                resultado_cadastro = cadastrar_produto(nome, preço)

                                if (resultado_cadastro["status"]):
                                    print(resultado_cadastro["mensagem"])
                                else:
                                    print('Erro ao cadastrar produto')

                    if(menu_opcao == 3):
                        listar_produtos()
                    
                    if(menu_opcao == 4):
                        item_id_a_deletar = int(input("Digite o id do item que deseja deletar: "))

                        status_id_produtos_database = check_id_produtos(item_id_a_deletar)

                        if status_id_produtos_database['status']:
                            resultado_deletar_produto = deletar_produto(item_id_a_deletar)
                            print(resultado_deletar_produto['mensagem'])
                        else:
                            print(status_id_produtos_database['mensagem'])

            else:
                contador_tentativas_login += 1

        