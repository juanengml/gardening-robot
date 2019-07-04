import csv
from time import sleep



class Database:
    def __init__(self,path,chave,valor):
        self.path = path
        self.chave = chave
        self.valor = valor

    def gravar_dado(self):
     with open(self.path,'a') as log:
            dados = [self.chave,self.valor]
            writer = csv.writer(log,delimiter=",")
            writer.writerow(dados[1])
            print "*" * 50
            print "\t\tGRAVADO no CSV"
            print "*" * 50
            #sleep(1)
