'''
Em um novo diretório crie um bd com três tabelas.
Tabela programadores (id, nome, idade e email)
Tabela habilidades (id e nome)
Tabela programador_habilidades (id, fk_programador e fk_habilidades)
'''

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///exercicio 03/programadores.db')

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programadores(Base):
    __tablename__ = 'programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer, index=True)
    email = Column(String(80), index=True)

    def __repr__(self):
        return f'<Programador: {self.id, self.nome}>:'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def excluir(self):
        db_session.delete(self)
        db_session.commit()


class Habilidades(Base):
    __tablename__ = 'habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)

    def __repr__(self):
        return f'<Habilidade: {self.id, self.nome}>:'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def excluir(self):
        db_session.delete(self)
        db_session.commit()


class Programadores_Habilidades(Base):
    __tablename__ = 'programadores_habilidades'
    id = Column(Integer, primary_key=True)
    fk_programadores = Column(Integer, ForeignKey('programadores.id'))
    fk_habilidades = Column(Integer, ForeignKey('habilidades.id'))

    def save(self):
        db_session.add(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()