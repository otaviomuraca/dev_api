from models import Programadores, Habilidades

def cadastrar_programador(nome:str, idade:int, email:str):
    programador = Programadores(nome=nome, idade=idade, email=email)
    print({
        'nome':nome,
        'idade':idade,
        'email':email
    })
    programador.save()

def listar_programadores():
    programadores = Programadores.query.all()
    print(programadores)

def consultar_programador(id:int):
    try:
        programador = Programadores.query.filter_by(id=id).first()
        print(programador)

    except AttributeError:
        print('Usuário com id não encontrado.')

def excluir_programador(id:int):
    try:
        programador = Programadores.query.filter_by(id=id).first()
        programador.excluir()
        print(f'O programador {programador.nome} foi excluído.')
    except AttributeError:
        print(f'Usuário com id não encontrado.')

def cadastrar_habilidade(nome:str):
    habilidade = Habilidades(nome=nome.lower())
    print(habilidade)
    habilidade.save()

def listar_habilidades():
    habilidades = Habilidades.query.all()
    print(habilidades)

def excluir_habilidade(nome:str):
    try:
        habilidade = Habilidades.query.filter_by(nome=nome).first()
        habilidade.excluir()
        print(f'A habilidade foi excluída.')
    except AttributeError:
        print(f"Usuário com id não encontrado.")



if __name__ == '__main__':
    cadastrar_programador('Otávio', 39, 'otaviomuraca@gmai.com')
    listar_programadores()
    #excluir_programador(2)
    consultar_programador(1)
    cadastrar_habilidade('Python')
    listar_habilidades()
    #excluir_habilidade(1)
    listar_habilidades()