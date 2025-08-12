from flask import Flask, jsonify
import os
import random

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
    return jsonify({"piadaAleatoria": piadas[randomico]})

@app.route("/piadas/<int:id_piada>")
def pegar_piada(id_piada):
    if id_piada in piadas:
        return jsonify(piadas[id_piada])
    else:
        return jsonify({"Erro": "Id de piada inexistente"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
