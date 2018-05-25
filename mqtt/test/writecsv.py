import csv
import random  
from time import sleep

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
           writer.writerow(line)


def sensores():
#  ID = random.choice(range())
  ID = 4
  MES = random.choice(range(1,2))
  DIA = random.choice(range(0,24))
  HORA = random.choice(range(24))
  UMIDADE = random.choice(range(75,100))
  #STATUS = "AGUADO"
  return "ID: %i; MES: %i; DIA: %i; Hora: %i; umidade: %i " % (ID,MES,DIA,HORA,UMIDADE)

def pre_processing(text):
 d = [] 
 dados = text.split("; ")
 for p in range(len(dados)):
    d.append(dados[p].split(":")[1])
 dados = [["ID", "MES", "DIA","Hora","umidade"],d]
 return dados


def gravar_dado(arquivo,text):
 with open(arquivo,'a') as log:
        dados = pre_processing(text)
        writer = csv.writer(log,delimiter=",")
        writer.writerow(dados[1])       
        print dados[1]
        sleep(0.01)

def main():
  while True:
   d = sensores()
   gravar_dado("plantacao.csv",d)

main()