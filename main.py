from fastapi import FastAPI
from controllers.pesquisa_usuario import listar_usuarios, cadastrar_usuario, pesquisa_usuario, check_nome_usuario,deletar_usuario
from controllers.usuarios import carregar_usuarios, validar_login
from controllers.produtos import carregar_produtos, listar_produtos, pesquisa_item, cadastrar_produto, deletar_produto, check_id_produtos

app = FastAPI()


@app.get("/")
def read_root():
    return 'Essa é minha API'

@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/usuarios/listar", description="Essa função lista usuarios")
def listar_usuario():
    result = listar_usuarios()
    return result

@app.post("/usuarios/add")
def adicionar_usuario(nome, email, senha):
    result = cadastrar_usuario(nome, email, senha)
    return result

@app.get("/usuarios/pesquisa/{nome}")
def pesquisar_nome(nome: str):
    result = pesquisa_usuario(nome)
    return result

@app.get("/usuarios/check/{nome}")
def check_nome(nome: str):
    result = check_nome_usuario(nome)
    return result

@app.delete("/usuarios/delete/{nome}")
def delete_usuario(nome):
    result = deletar_usuario(nome)
    return result

@app.get("/usuarios/carregar")
def carregar_todos_usuarios():
    result = carregar_usuarios()
    return result

@app.get("/usuarios/validar/{email}/{senha}")
def conferir_login(email, senha):
    result = validar_login(email, senha)
    return result

@app.get("/produtos/carregar")
def carregar_todos_produtos():
    result = carregar_produtos()
    return result

@app.get("/produtos/listar")
def listar_produto():
    result = listar_produtos()
    return result

@app.get("/produtos/pesquisa/item")
def pesquisa_produto(nome_item):
    Result = pesquisa_item(nome_item)
    return Result

@app.post("/produtos/cadastrar/produto")
def cadastrar_item(nome, preco):
    result = cadastrar_produto(nome, preco)
    return result

@app.delete("/produtos/deletar/produto")
def delete_produto(produto_id):
    result = deletar_produto(produto_id)
    return result

@app.get("/produtos/check/produto")
def check_produtos(id):
    result = check_id_produtos(id)
    return result