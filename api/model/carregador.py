import pandas as pd


class Carregador:

    def carregar_dados(self, url: str):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros
        no read_csv que poderiam ser utilizados para dar opções
        adicionais.
        """
        return pd.read_csv(url, delimiter=';')
    