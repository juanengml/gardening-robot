from serial import Serial
from datetime import datetime
import csv
import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import ast

try:
 ser = Serial("/dev/ttyUSB0",9600)
except:
 ser = Serial("/dev/ttyUSB1",9600)

THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'jxvHtpYfVmfUOSuefstq'
INTERVAL=2
#import model

"""
gpio_state = {1: False, 2: False}

def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code ' + str(rc))
    client.subscribe('v1/devices/me/rpc/request/+')
    client.publish('v1/devices/me/attributes', get_gpio_status(), 1)

def on_message(client, userdata, msg):
    print 'Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload)
    data = json.loads(msg.payload)
    if data['method'] == 'getGpioStatus':
        client.publish(msg.topic.replace('request', 'response'), get_gpio_status(), 1)
    elif data['method'] == 'setGpioStatus':
        set_gpio_status(data['params']['pin'], data['params']['enabled'])
        client.publish(msg.topic.replace('request', 'response'), get_gpio_status(), 1)
        client.publish('v1/devices/me/attributes', get_gpio_status(), 1)


def get_gpio_status():
    return json.dumps(gpio_state)


def set_gpio_status(pin, status):
    print pin,status
    if pin == 1 and status == True:
        ser.write("w")
    if pin == 1 and status == False:
        ser.write("q")
    if pin == 2 and status == True:
        ser.write("r")
    if pin == 2 and status == False:
        ser.write("e")
    gpio_state[pin] = status
"""
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
        print json.dumps(sensor_data)

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except:
    pass


client.loop_stop()
client.disconnect()
