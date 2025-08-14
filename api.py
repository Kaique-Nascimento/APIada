from flask import Flask, Response
from flask_cors import CORS
import os
import random
import json

app = Flask(__name__)
CORS(app)
piadas = {
    1: {"piada": "Sua mãe é tão gorda, mas tão gorda, que ela precisa comprar roupa na 'VestCasa'"},
    2: {"piada": "Sua mãe é tão burra, mas tão burra, que ela roubou amostra grátis"},
    3: {"piada": "Hoje na nossa loja temos Promoção, Promocinho e Provizinho!"},
    4: {"piada": "Eu sou muito bom em engenharia quântica, química e em contar mentiras"},
}

@app.route("/")
def root():
    randomico = random.randint(1, len(piadas))
    resposta = json.dumps({"piadaAleatoria": piadas[randomico]}, ensure_ascii=False)
    return Response(resposta, mimetype='application/json')

@app.route("/piadas/<int:id_piada>")
def pegar_piada(id_piada):
    if id_piada in piadas:
        resposta = json.dumps(piadas[id_piada], ensure_ascii=False)
        return Response(resposta, mimetype='application/json')
    else:
        erro = json.dumps({"Erro": "Id de piada inexistente"}, ensure_ascii=False)
        return Response(erro, mimetype='application/json'), 404
    
@app.route("/piadas/todas")
def listar_piadas():
        resposta = json.dumps(piadas, ensure_ascii=False)
        return Response(resposta, mimetype='application/json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    CORS(app, origins=["http://127.0.0.1:5500"])

