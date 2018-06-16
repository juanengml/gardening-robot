# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt

import csv
import random  
from time import sleep

import os 
TOPIC = "#"
def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
           writer.writerow(line)



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
        print "*" * 50
        print "GRAVADO no CSV"
        print "*" * 50
        sleep(1)


def my_ip():
    ip = os.popen("ip a | grep 192").read()
    pi = ip.find("1")
    pf = ip.find("/")
    me = ip[pi:pf]
    return me


def on_connect(self,client, data, rc):
    self.subscribe([(TOPIC,0)])

# função chamada quando uma nova mensagem do tópico é gerada
def on_message(client, userdata, msg):
    # decodificando o valor recebido
    
    #print msg.topic + "/" + str(v)
    
    print "TOPICO: ",msg.topic
    print "payload: ",str(msg.payload)
    text = str(msg.payload)
    gravar_dado("plantacao.csv",text)
    
        


# clia um cliente para supervisã0
client = mqtt.Client()

# estabelece as funçõe de conexão e mensagens
client.on_connect = on_connect
client.on_message = on_message

# conecta no broker
client.connect("192.168.100.31", 1883)

# permace em loop, recebendo mensagens
client.loop_forever()
