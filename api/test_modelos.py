from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
pre_processador = PreProcessador()
modelo = Modelo()
avaliador = Avaliador()

# Parâmetros
url_dados = ('/content/DataClientesNew.csv')

percentual_teste = 0.2

# Código

# Carga
dataset = carregador.carregar_dados(url_dados)
# Pré-processamento
X_train, X_test, Y_train, Y_test = pre_processador.pre_processar(dataset,
                                                               percentual_teste)



def test_modelo_knn():  

    # Parâmetros
    url_dados = ('/content/DataClientesNew.csv')

    percentual_teste = 0.2

    # Código

    # Carga
    dataset = carregador.carregar_dados(url_dados)
    # Pré-processamento
    X_train, X_test, Y_train, Y_test = pre_processador.pre_processar(dataset,
                                                                percentual_teste)
