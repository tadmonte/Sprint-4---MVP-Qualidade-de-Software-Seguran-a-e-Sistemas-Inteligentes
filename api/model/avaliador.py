from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Avaliador:

    def avaliar_acuracia(self, modelo, X_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = modelo.predict(X_test)   
        return (predicoes)
