from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base



class Avaliacao(Base):
    __tablename__ =  'avaliacoes'
    
    id = Column(Integer, primary_key=True)
    
    receita_total = Column("Receita Total", Integer)
    pedidos_feitos = Column("Pedidos Feitos", Integer)
    limite = Column("Limite", Integer)
    target = Column("Target", Integer)
    resultado = Column("Avaliação", Integer)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, receita_total:int, pedidos_feitos:int, limite:int, target:str,
                 resultado:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um avaliacao

        Arguments:
        name: nome do avaliacao
            preg: número de gestações
            plas: concentração de glicose
            pres: pressão sanguínea
            skin: espessura da pele
            test: insulina
            mass: índice de massa corporal
            pedi: função pedigree
            age: idade
            outcome: diagnóstico
            data_insercao: data de quando o avaliacao foi inserido à base
        """
        
        self.receita_total = receita_total
        self.pedidos_feitos = pedidos_feitos
        self.limite = limite
        self.target = target
        self.resultado = resultado
      

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao