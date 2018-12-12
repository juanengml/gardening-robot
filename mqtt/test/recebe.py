# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt

import csv
import random  
from time import sleep

import os 
TOPIC = "#"

def on_connect(self,client, data, rc):
    self.subscribe([(TOPIC,0)])

def on_message(client, userdata, msg):
    print "TOPICO: ",msg.topic," payload: ",str(msg.payload)
    sleep(0.5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.100.3", 1883)
client.loop_forever()
