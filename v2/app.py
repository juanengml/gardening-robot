from serial import Serial
from datetime import datetime
import db
import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import ast
from os import system
import csv


path = "dba.csv"

try:
 ser = Serial("/dev/ttyUSB0",9600)
except:
 ser = Serial("/dev/ttyUSB1",9600)

#THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'jxvHtpYfVmfUOSuefstq'
THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
#ACCESS_TOKEN = 'vHXgIJCOkDqcuuJQwjd0'
INTERVAL=2
ID = 1


def Tempo():
    hora = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    dia = datetime.now().day
    mes = datetime.now().month
    ano = datetime.now().year
    return "%s/%s/%s %s:%s:%s" % (dia,mes,ano,hora,minute,second)


def gravar_dado(path,chave,valor):
 with open(path,'a') as log:
        dados = [chave,valor]
        writer = csv.writer(log,delimiter=",")
        writer.writerow(dados[1])
        print "*" * 50
        print "\t\tGRAVADO no CSV"
        print "*" * 50


def tratamento(msg):
    dicionario = ast.literal_eval(str(msg.split("\r\n")[0]))
    try:
           return dicionario
    except:
         pass

def preditor(dicionario):
    a = dicionario.keys()[0]
    data = dicionario.values()
    for p in range(len(data)):
        print data[p]
        #print model.predict(data[p])

next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
#client.on_connect = on_connect
#client.on_message = on_message
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
    while True:
        text = ser.readline()
        sensor_data = tratamento(text)
        valores =  sensor_data.values()
        chaves = sensor_data.keys()
        valores.insert(0,ID)
        chaves.insert(0,"ID")
        valores.insert(1,Tempo())
        chaves.insert(1,"datetime")
        #gravar_dado("dba.csv",chave,valor)
        #system("echo %s >> dba.csv" % "".join(valores))
        print chaves,valores
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except:
    pass


client.loop_stop()
client.disconnect()
