import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from datetime import datetime

df = pd.read_csv('../v1/plantacao.csv')

X = np.array(df.drop('ID',axis = 1))
y = np.array(df["ID"])

knn = KNeighborsClassifier(n_neighbors=4)
kmeans = KMeans(n_clusters=4,random_state=0)
clusterer = GaussianMixture(n_components=4,random_state=0)

class Model:
    def __init__(self,lista):
        self.lista = lista

    def treinar(self):
        print "Treinando Modelo ...."
        knn.fit(X,y)
        kmeans.fit(X,y)
        clusterer.fit(X,y)

    def predicao(self):
      nivel =  [knn.predict([self.lista])[0],  kmeans.predict([self.lista])[0],  clusterer.predict([self.lista])[0]]
      pred_status = {"KNN":nivel[0],"KMeans":nivel[1],"cluster":nivel[2]}
      return pred_status
