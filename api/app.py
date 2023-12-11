from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from model.avaliacao import Avaliacao
from model import Session
from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model
from model.preprocessador import PreProcessador
from logger import logger
from schemas import *
from flask_cors import CORS



# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
avaliacao_tag = Tag(name="Avaliação", description="Adição, visualização, remoção e predição de Avaliacao com Diabetes")

# Carregando modelo
ml_path = './database/DataClientesNew.csv'

percentual_teste = 0.2
# Carga
dataset = Carregador().carregar_dados(ml_path)
# Pré-processamento
X_train, X_test, Y_train, Y_test = PreProcessador().pre_processar(dataset,
                                                            percentual_teste)                                   
# Treinamento do modelo
model = Model().treinar_KNN(X_train, Y_train)

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de Avaliacao
@app.get('/avaliacoes', tags=[avaliacao_tag],
         responses={"200": AvaliacaoViewSchema, "404": ErrorSchema})
def get_avaliacoes():
    """Lista todos os Avaliacao cadastrados na base
    Retorna uma lista de Avaliacao cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de Avaliacao cadastrados na base
    """
    session = Session()
    
    # Buscando todos os Avaliacao
    avaliacoes = session.query(Avaliacao).all()
    
    if not avaliacoes:
        logger.warning("Não há Avaliacao cadastrados na base :/")
        return {"message": "Não há Avaliacao cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d Avaliacao econtrados" % len(avaliacoes))
        return apresenta_avaliacoes(avaliacoes), 200


@app.delete('/avaliacao', tags=[avaliacao_tag], responses={"200": None, "404": ErrorSchema})
def delete(query: AvaliacaoDeleteSchema):
    """Remove uma avaliação pelo seu id
    """
    # Criando conexão com a base
    session = Session()
    # Adicionando paciente
    row_to_delete = session.query(Avaliacao).filter(Avaliacao.id == query.id).first()

    if row_to_delete is not None:
        # Delete the row
        session.delete(row_to_delete)

        # Commit the transaction
        session.commit()
        return "", 200
    else:
        error_msg = "Não foi possível encontrar o item :/"
        logger.warning(f"Erro ao remover avaliação '{query.id}', {error_msg}")
        return {"message": error_msg}, 404


# Rota de adição de paciente
@app.post('/avaliacao', tags=[avaliacao_tag],
          responses={"200": AvaliacaoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: AvaliacaoSchema):
    """Adiciona uma nova avaliação à base de dados
    """
    
    resultado = (Avaliador().avaliar_acuracia(model, [
        [form.receita_total, form.pedidos_feitos, form.limite, form.target]
    ]))
    print(resultado)
    avaliacao = Avaliacao(
        receita_total=form.receita_total,
        pedidos_feitos=form.pedidos_feitos,
        limite=form.limite,
        target=form.target,
        resultado=resultado[0],
    )

    logger.debug(f"Adicionando avaliação: '{avaliacao.id}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando paciente
        session.add(avaliacao)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionando avaliação: '{avaliacao.id}'")
        return apresenta_avaliacao(avaliacao), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar avaliação '{avaliacao.id}', {error_msg}")
        return {"message": error_msg}, 400
    


    
