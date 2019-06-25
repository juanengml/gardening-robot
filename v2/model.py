import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import seaborn as sns


df = pd.read_csv('../v1/plantacao.csv')


#print df.drop('ID',axis = 1)
X = np.array(df.drop('ID',axis = 1))
y = np.array(df["ID"])


from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from datetime import datetime

knn = KNeighborsClassifier(n_neighbors=4)
kmeans = KMeans(n_clusters=4,random_state=0)
clusterer = GaussianMixture(n_components=4,random_state=0)

def predicao(lista):
  knn.fit(X,y)
  kmeans.fit(X,y)
  clusterer.fit(X,y)
  # 0 - knn
  # 1 - KMeans
  # 2 - GaussianMixture
  nivel =  [knn.predict([lista])[0],kmeans.predict([lista])[0],clusterer.predict([lista])[0]]
  pred_status = {"KNN":nivel[0],"KMeans":nivel[1],"cluster":nivel[2]}
  return pred_status



def time():
    hora = datetime.now().hour
    mes = datetime.now().month
    dia = datetime.now().day
    return [mes,dia,hora]

def predict(data):
 tempo = time()
 lista = [tempo[0],tempo[1], tempo[2], data]
 pred = predicao(lista)
 return pred
