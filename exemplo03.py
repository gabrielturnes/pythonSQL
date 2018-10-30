# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("sqlite:///lab05-ex01.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Pessoa = Base.classes.Pessoa
    Telefones = Base.classes.Telefones

    lista_de_pessoas = session.query(Pessoa).join(Telefones).all()

    for linha in lista_de_pessoas:
        print("id: {}\t nome: {}\t".format(linha.idPessoa, linha.nome))
        for tel in linha.telefones_collection:
            print("Telefone: {}".format(tel.numero))
