from flask import Flask, Response
from flask_cors import CORS
import os
import random
import certifi
from dotenv import load_dotenv
import json
from pymongo import MongoClient

#load_dotenv()

app = Flask(__name__)
CORS(app)
link = os.getenv('LINKDB')
conexao = MongoClient(link)
db = conexao.get_database("dbpiadas")
colecao = db.get_collection("piadas")
client = MongoClient(link, tlsCAFile=certifi.where())

@app.route("/")
def root():
    piadas = list(colecao.find())
    
    if not piadas:
        return Response(json.dumps({"Erro": "Nenhuma piada encontrada"}), mimetype='application/json', status=404)
    
    piada_aleatoria = random.choice(piadas)
    
    resposta = json.dumps({"piadaAleatoria": piada_aleatoria["piada"]}, ensure_ascii=False)
    return Response(resposta, mimetype='application/json')

#@app.route("/piadas/<int:id_piada>")
#def pegar_piada(id_piada):
#    if id_piada in piadas:
#        resposta = json.dumps(piadas[id_piada], ensure_ascii=False)
#        return Response(resposta, mimetype='application/json')
#    else:
#        erro = json.dumps({"Erro": "Id de piada inexistente"}, ensure_ascii=False)
#        return Response(erro, mimetype='application/json'), 404
    
@app.route("/piadas/todas")
def listar_piadas():
        resposta = ""
        piadas = list(colecao.find())
        for piada in piadas:
            print(piada['piada'])
            resposta += json.dumps(piada['piada'], ensure_ascii=False) + "\n"
        return Response(resposta, mimetype='application/json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    CORS(app, origins=["http://127.0.0.1:5500"])

