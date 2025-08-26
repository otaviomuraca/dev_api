import json


from flask import Flask, request
from flask_restful import Resource, Api


from habilidades import Habilidades, ListaHabilidades, ChecarHabilidades


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {'id': 1, 'nome':'Otavio',
     'habilidades':['Python',"Flask"]},
    {'id': 2, 'nome':'Rafa',
     'habilidades':['Python',"Django"]},
    {'id': 3, 'nome':'Mariana',
     'habilidades':['JavaScript',"React","Node.js"]},
    {'id': 4, 'nome':'Lucas',
     'habilidades':['Java',"Spring Boot","SQL"]},
    {'id': 5, 'nome':'Carla',
     'habilidades':['C#',"ASP.NET","Azure"]},
    {'id': 6, 'nome':'Diego',
     'habilidades':['Python',"Pandas","NumPy","ETL"]},
    {'id': 7, 'nome':'Fernanda',
     'habilidades':['Go',"Docker","Kubernetes"]},
    {'id': 8, 'nome':'João',
     'habilidades':['PHP',"Laravel","MySQL"]},
    {'id': 9, 'nome':'Beatriz',
     'habilidades':['Ruby',"Rails","PostgreSQL"]},
    {'id': 10, 'nome':'Gustavo',
     'habilidades':['TypeScript',"Angular","Firebase"]}
]


class Desenvolvedor(Resource):
    def get(self, id):
        return desenvolvedores[id]

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return desenvolvedores[id]

    def delete(self, id):
        desenvolvedores.pop(id)
        return f"desenvolvedor {id} deletado com sucesso."

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades/' )
api.add_resource(Habilidades, '/habilidades/<int:id>' )
api.add_resource(ChecarHabilidades, '/habilidades/<habilidade>')

if __name__ == '__main__':
    app.run(debug=True)