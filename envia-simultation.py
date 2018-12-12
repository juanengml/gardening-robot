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
niveis = {1:"arido",
 2:"seco",
 3:"umido",
 4:"molhado"}


while True:
    menu = pyautogui.confirm(text='Status Janela',
        title='Simulador MQTT', buttons=['bombas', 'reset','SAIR'])
        #buttons=['arido', 'seco','umido','molhado','SAIR','reset'])
    
    if menu=='bombas':
     menu = pyautogui.confirm(text='Selecione sua bomba',title='Simulador MQTT', buttons=['1', '2','SAIR'])
     if menu == '1' or menu == '2':
       entrada = pyautogui.prompt(text='Digite quantos segundos de ativação', title='Timer' , default='')
       print menu,entrada
       client.publish("/garden/painel/bombas/ID/"+menu, entrada)
    if menu=='reset':
       print menu
       client.publish("/garden/painel/reset/status/", '0')
       sleep(5)
       client.publish("/garden/painel/reset/status/", '1')
     
       
    if menu=='SAIR': 
        print "EXIT PROGRAMMM"
        break


  