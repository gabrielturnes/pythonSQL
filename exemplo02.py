# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("sqlite:///teste.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Contato = Base.classes.Contato

    lista_de_contatos = session.query(Contato).all()

    for linha in lista_de_contatos:
        print("id: {}\t nome: {}\t telefone: {}".format(linha.idContato, linha.nome, linha.telefone))

    print("Outra pessoa")
    pessoa = session.query(Contato).filter(and_(Contato.nome == "Gabriela", Contato.telefone == "(48)998015730")).first()
    print("id: {}\t nome: {}\t telefone: {}".format(pessoa.idContato, pessoa.nome, pessoa.telefone))

    pessoa.nome = 'Gabriel'
    session.commit()