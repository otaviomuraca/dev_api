'''
Acrescentar na API de habilidades (módulo habilidades) os métodos PUT, POST e DELETE

O método POST deverá inserir uma nova habilidade na lista

O método PUT a partir de um ID(identificação da posição) deverá alterar o nome da habilidade que está naquela posição

O método DELETE deverá deletar uma habilidade que esteja na posição informada na requisição

Incluir validação no app-restful para verificar se a habilidade informada existe na lista de habilidades.
'''


import json

from flask import Flask, request
from flask_restful import Resource

lista_habilidades = [
    {'id': 1, 'habilidade': "Python"},
    {'id': 2, 'habilidade': "Flask"},
    {'id': 3, 'habilidade': "Django"},
    {'id': 4, 'habilidade': "JavaScript"},
    {'id': 5, 'habilidade': "React"},
    {'id': 6, 'habilidade': "Node.js"},
    {'id': 7, 'habilidade': "Java"},
    {'id': 8, 'habilidade': "Spring Boot"},
    {'id': 9, 'habilidade': "SQL"},
    {'id': 10, 'habilidade': "C#"},
    {'id': 11, 'habilidade': "ASP.NET"},
    {'id': 12, 'habilidade': "Azure"},
    {'id': 13, 'habilidade': "Pandas"},
    {'id': 14, 'habilidade': "NumPy"},
    {'id': 15, 'habilidade': "ETL"},
    {'id': 16, 'habilidade': "Go"},
    {'id': 17, 'habilidade': "Docker"},
    {'id': 18, 'habilidade': "Kubernetes"},
    {'id': 19, 'habilidade': "PHP"},
    {'id': 20, 'habilidade': "Laravel"},
    {'id': 21, 'habilidade': "MySQL"},
    {'id': 22, 'habilidade': "Ruby"},
    {'id': 23, 'habilidade': "Rails"},
    {'id': 24, 'habilidade': "PostgreSQL"},
    {'id': 25, 'habilidade': "TypeScript"},
    {'id': 26, 'habilidade': "Angular"},
    {'id': 27, 'habilidade': "Firebase"}
]

class Habilidades(Resource):
    def get(self, id):
        return lista_habilidades[id]

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return lista_habilidades[id]

    def delete(self, id):
        posicao = id - 1
        lista_habilidades.pop(posicao)
        return f'Habilidade excluída com sucesso.'



class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] =  posicao + 1
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]


class ChecarHabilidades(Resource):
    def get(self, habilidade):
        habilidade = habilidade.lower()
        if habilidade:
            if any(h['habilidade'].lower()  == habilidade for h in lista_habilidades):
                resposta = f'A habilidades {habilidade} está na lista. '
            else:
                resposta = f'A habilidades {habilidade} NÃO está na lista. '

            return resposta

        else:
            return 'Habilidade não informada'