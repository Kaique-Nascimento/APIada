from flask import Flask, Response
import os
import random
import json

app = Flask(__name__)

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
