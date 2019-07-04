from serial import Serial
from datetime import datetime
import csv
import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import ast
from os import system

try:
 ser = Serial("/dev/ttyUSB0",9600)
except:
 ser = Serial("/dev/ttyUSB1",9600)

THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'jxvHtpYfVmfUOSuefstq'
#THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
#ACCESS_TOKEN = 'vHXgIJCOkDqcuuJQwjd0'
INTERVAL=2

def tempo():
  hora = "%s:%s" (datetime.now().hour,datetime.now().minute)
  data = "%s\\%s\\%s" % (datetime.now().day,datetime.now().month,datetime.now(),year)
  Tempo = "%s %s;" % (data,hora)
  return Tempo

def tratamento(msg):
    dicionario = ast.literal_eval(str(msg.split("\r\n")[0]))
    try:
         if dicionario.keys()[0] == "Temperature":
           return dicionario
         else:
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
        #preditor(text)
        #data = tempo() + json.dumps(sensor_data)
        #print data
        print json.dumps(sensor_data)
        system("echo %s >> data1.csv" %  json.dumps(sensor_data))

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except:
    pass


client.loop_stop()
client.disconnect()
