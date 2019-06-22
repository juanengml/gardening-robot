# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt
import random
from time import sleep
import datetime
import pyautogui

client = mqtt.Client()
# conecta no broker
client.connect("192.168.100.3", 1883)

# "bloco/E/lab/302/SENSOR/JANELA/1
# "home/sala/janela/01/status/"
while True:
    menu = pyautogui.confirm(text='Status Janela', title='Simulador MQTT', buttons=['led1-ON', 'led1-OFF',"SAIR"])
    
    #client.publish("/makete/",menu)
    if menu=="led1-ON":
        client.publish("/garden/painel/","o")
    if menu=="led1-OFF":
        client.publish("/garden/painel/","a")
    if menu=='SAIR': 
        print "EXIT PROGRAMMM"
        break