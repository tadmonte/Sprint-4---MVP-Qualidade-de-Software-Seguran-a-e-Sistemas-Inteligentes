from pydantic import BaseModel
from typing import Optional, List
from model.avaliacao import Avaliacao
import json
import numpy as np

class AvaliacaoSchema(BaseModel):
    """ Define como um novo Avaliacao a ser inserido deve ser representado
    """
    receita_total: float = 148.8
    pedidos_feitos: int = 1
    limite: int = 72
    target: int = 35
    
class AvaliacaoDeleteSchema(BaseModel):
    id: int = 1
    
class AvaliacaoViewSchema(BaseModel):
    """Define como um Avaliacao será retornado
    """
    id: int = 1
    receita_total: int = 2
    pedidos_feitos: int = 148
    limite: int = 72
    target: int = 35
    resultado:int=1

    
    
    


class ListaAvaliacaosSchema(BaseModel):
    """Define como uma lista de Avaliacaos será representada
    """
    Avaliacaos: List[AvaliacaoSchema]

    

    
# Apresenta apenas os dados de um Avaliacao    
def apresenta_avaliacao(Avaliacao: Avaliacao):
    """ Retorna uma representação do Avaliacao seguindo o schema definido em
        AvaliacaoViewSchema.
    """
    return {
        "id": Avaliacao.id,
        "pedidos_feitos": Avaliacao.pedidos_feitos,
        "limite": Avaliacao.limite,
        "target": Avaliacao.target,
        "receita_total": Avaliacao.receita_total,
        "resultado": Avaliacao.resultado,
        
    }
    
# Apresenta uma lista de Avaliacaos
def apresenta_avaliacoes(Avaliacaos: List[Avaliacao]):
    """ Retorna uma representação do Avaliacao seguindo o schema definido em
        AvaliacaoViewSchema.
    """
    result = []
    for Avaliacao in Avaliacaos:
        result.append({
            "id": Avaliacao.id,
            "pedidos_feitos": Avaliacao.pedidos_feitos,
            "limite": Avaliacao.limite,
            "target": Avaliacao.target,
            "receita_total": Avaliacao.receita_total,
            "resultado": Avaliacao.resultado,
        })

    return {"avaliacoes": result}

