import db
import ast
from serial import Serial
from datetime import datetime
import time
import paho.mqtt.client as mqtt
import json


try:
 ser = Serial("/dev/ttyUSB0",9600)
except:
 ser = Serial("/dev/ttyUSB1",9600)

def Tempo():
    hora = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    dia = datetime.now().day
    mes = datetime.now().month
    ano = datetime.now().year
    return "%s/%s/%s %s:%s:%s" % (dia,mes,ano,hora,minute,second)


def tratamento(msg):
    dicionario = ast.literal_eval(str(msg.split("\r\n")[0]))
    try:
           return dicionario
    except:
         pass


#THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'jxvHtpYfVmfUOSuefstq'
THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
#ACCESS_TOKEN = 'vHXgIJCOkDqcuuJQwjd0'
INTERVAL=2

next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
#client.on_connect = on_connect
#client.on_message = on_message
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

ID = 1
path = "dba.csv"
def main():
 while True:
    text = ser.readline()
    sensor_data = tratamento(text)
    valores =  sensor_data.values()
    chaves = sensor_data.keys()
    valores.insert(0,ID)
    chaves.insert(0,"ID")
    valores.insert(1,Tempo())
    chaves.insert(1,"datetime")
    #print chaves,valores
    banco = db.Database(path,chaves,valores)
    banco.gravar_dado()
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    print chaves,valores



main()
client.loop_stop()
client.disconnect()
