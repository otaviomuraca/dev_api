from models import Pessoas


def cadastrar_pessoas():
    pessoa = Pessoas(nome="Leonardo", idade="39")
    print(pessoa)
    pessoa.save()

def listar():
    pessoa = Pessoas.query.all()
    print(pessoa)

def consultar(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    # SELECT * FROM pessoas WHERE nome = :nome LIMIT 1;
    #.first() retorna a primeira a primeira linha encontrada
    print({'Nome':pessoa.nome,'idade':pessoa.idade})

def atualizar(id:int, novo_nome:str, nova_idade:int):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.id = id
    pessoa.nome = novo_nome
    pessoa.idade = nova_idade
    pessoa.save()

def excluir(id:int):
    pessoa = Pessoas.query.filter_by(id=id).first()
    pessoa.excluir()
    print(f"Usuário {pessoa.nome} deletado com sucesso.")


if __name__ == '__main__':
    #cadastrar_pessoas()
    #consultar('Leonardo')
    listar()
    #atualizar(1, 'Joana', 14) #id, nome, idade
    listar()
    excluir(6)