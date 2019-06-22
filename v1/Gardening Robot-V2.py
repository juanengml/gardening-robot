# coding: utf-8

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import seaborn as sns

df = pd.read_csv('plantacao.csv')

X = np.array(df.drop('ID',axis = 1))

y = np.array(df["ID"])

knn = KNeighborsClassifier(n_neighbors=4).fit(X,y)

distances, indices = knn.kneighbors(X)
#sns.pointplot(data=indices)

def predicao(lista):
 nivel =  knn.predict([lista])
 if nivel[0] == 1: return "arido"
 if nivel[0] == 2: return "seco"
 if nivel[0] == 3: return "umido"
 if nivel[0] == 4: return "molhado"

def new_sensor_data():
 MES = raw_input("MES: ")
 DIA = raw_input("DIA: ")
 Hora = raw_input("Hora: ")
 umidade = raw_input("umidade ")
 lista = [MES,DIA, Hora, umidade]
 return lista

def main():
    dados = new_sensor_data()
    pred = predicao(dados)
    print dados
    print pred
    

main()

