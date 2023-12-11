import numpy as np
import pickle
import joblib
from sklearn.neighbors import KNeighborsClassifier

class Model:

    def treinar_KNN(self, X_train, Y_train):
        """ Cria e treina um modelo SVM. Poderia ter um Grid Search
        com cross_validation para escolher os melhores hiperparâmetros, etc.
        """
        modelo = KNeighborsClassifier()
        modelo.fit(X_train, Y_train)
        return modelo