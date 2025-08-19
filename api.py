from flask import Flask, Response
from flask_cors import CORS
import os
import random
import json
import certifi

from pymongo import MongoClient

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])

# Conexão com MongoDB Atlas
link = os.environ.get('LINKDB')
client = MongoClient(
    link,
    tls=True,
    tlsCAFile=certifi.where()
)
colecao = MongoClient(link, tls=True, tlsAllowInvalidCertificates=True).get_database("dbpiadas").get_collection("piadas")

@app.route("/")
def root():
    piadas = list(colecao.find())
    if not piadas:
        return Response(json.dumps({"Erro": "Nenhuma piada encontrada"}), mimetype='application/json', status=404)
    
    piada_aleatoria = random.choice(piadas)
    resposta = json.dumps({"piadaAleatoria": piada_aleatoria["piada"]}, ensure_ascii=False)
    return Response(resposta, mimetype='application/json')

@app.route("/piadas/todas")
def listar_piadas():
    piadas = list(colecao.find())
    todas = [piada['piada'] for piada in piadas]
    return Response(json.dumps(todas, ensure_ascii=False), mimetype='application/json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
