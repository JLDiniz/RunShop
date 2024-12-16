from fastapi import FastAPI
from controllers.pesquisa_usuario import listar_usuarios, cadastrar_usuario, pesquisa_usuario

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
