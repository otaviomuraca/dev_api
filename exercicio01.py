'''
Desenvolva uma API que gerencia um cadastro de tarefas.

A API terá uma lista de tarefas que deverá ter os seguintes campos: id, responsável, tarefa e status.

A API deverá permitir listar todas as tarefas e também incluir novas tarefas.

A API deverá permitir consultar uma tarefa através do ID, alterar o status de uma tarefa e também excluir a tarefa.

Nenhuma outra alteração deverá ser pemitida além do status da tarefa.

'''

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas =  [{
    'id':'1',
    'responsavel':'Otávio',
    'tarefa':'Exercício de Flask',
    'status':'pendente'

}]

@app.route('/tarefas/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def gerenciar_tarefas(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':'Tarefa não encontrada.'}
        except Exception:
            response = 'Erro desconhecido. Procure o administrador.'
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro deletado.'})


@app.route('/tarefas/', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas/novatarefa/', methods=['POST'])
def nova_tarefas():
    dados = json.loads(request.data)
    tarefas.append(dados)
    return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)