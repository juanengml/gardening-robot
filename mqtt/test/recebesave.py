# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt

import csv
import random  
from time import sleep
from datetime import datetime 
import time


def millis():
        return time.time() * 1000

import os 

TOPIC = "home/gardem/horta/planta/#"

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
           writer.writerow(line)



def pre_processing(text):
 d = [] 
 features = (" ".join(text.split(" umidade: "))).split("; ")
 dados = [["ID", "MES", "DIA","Hora","umidade"], features]
 return dados

def gravar_dado(arquivo,text):
 with open(arquivo,'a') as log:
        dados = pre_processing(text)
        writer = csv.writer(log,delimiter=",")
        writer.writerow(dados[1])       
        print "*" * 50
        print "\tGRAVADO no CSV"
        print "*" * 50
         





def on_connect(self,client, data, rc):
    self.subscribe([(TOPIC,0)])

# função chamada quando uma nova mensagem do tópico é gerada
def on_message(client, userdata, msg):
    # decodificando o valor recebido
    
    #print msg.topic + "/" + str(v)
    
    print "TOPICO: ",msg.topic," payload: ",str(msg.payload)
    ID = "%s" % (str(msg.topic).split("/"))[4]
    text = "%s" % (str(msg.payload))
    mes, dia, hora = datetime.now().month, datetime.now().day, datetime.now().hour
    #text =   "%s; %s; %s; %s; %s" % (ID,mes,dia,hora,text[6:])
    dado = "%s; %s; %s; %s; %s" % (ID,mes,dia,hora,text[6:])
    #print dado
    #sleep(0.5)
    start = millis()
    while ( (start + 1000) > millis() ):
        pass
    gravar_dado("log.csv",dado)

    
        


# clia um cliente para supervisã0
client = mqtt.Client()

# estabelece as funçõe de conexão e mensagens
client.on_connect = on_connect
client.on_message = on_message

# conecta no broker
client.connect("192.168.100.3", 1883)

# permace em loop, recebendo mensagens
client.loop_forever()
