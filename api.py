from fastapi import FastAPI
from random import randint

app = FastAPI()

piadas = {
    1: {"piada" : "Sua mãe é tão gorda, mas tão gorda, que ela precisa comprar roupa na 'VestCasa'"},
    2: {"piada" : "Sua mãe é tão burra, mas tão burra, que ela roubou amostra grátis"},
    3: {"piada" : "Hoje na nossa loja temos Promoção, Promocinho e Provizinho!"},
    4: {"piada" : "Eu sou muito bom em engenharia quântica, química e em contar mentiras"},
}

@app.get("/")
async def root():
    randomico = randint(1, len(piadas))
    return {"piadaAleatoria" : piadas[randomico]}


@app.get("/piadas/{id_piada}")
def pegar_piada(id_piada:int):
    if id_piada in piadas:

        return piadas[id_piada]
    else:
        return {"Erro":"Id de piada inexistente"}