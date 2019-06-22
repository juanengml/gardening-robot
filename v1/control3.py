import pyupm_i2clcd as lcd  # importa biblioteca para i2c 
import mraa
import time                
import paho.mqtt.client as mqtt
import random

def color():
  return random.choice(range(256))

TOPIC = "/garden/painel/#"

Lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
Lcd.clear() 
Lcd.setColor(color(), color(), color()) 

time.sleep(1)

d6 = mraa.Gpio(6)        
bomba01 = mraa.Gpio(2)        
bomba02 = mraa.Gpio(3)        

time.sleep(1)

d6.dir(mraa.DIR_OUT)   
bomba01.dir(mraa.DIR_OUT)   
bomba02.dir(mraa.DIR_OUT)   

time.sleep(0.5)
d6.write(0)      ## Pino 6 de resetar 
bomba01.write(1) ## desligada
bomba02.write(1) ## desligada

Lcd.clear()
Lcd.setCursor(0,0)
#Lcd.write(sensor)
#Lcd.setCursor(1,0)
Lcd.write("  GARDEN START")


def on_connect(self,client, data, rc):
    self.subscribe([(TOPIC,0)])

def on_message(client, userdata, msg):
    print "TOPICO: ",msg.topic," payload: ",str(msg.payload)
    if "/garden/painel/reset/status/" == msg.topic:
        Lcd.setCursor(0,0)
        Lcd.clear()
        if str(msg.payload) == '1':
          Lcd.setCursor(0,0)
          Lcd.write("  GARDEN [DOWN]")
          d6.write(1)
        else:
          Lcd.setCursor(0,0)
          Lcd.write("  GARDEN [UP]")
          d6.write(0)    

    if "/garden/painel/bombas/ID/" in msg.topic:
        print (msg.topic).split("ID/")[1],msg.payload+"s"
        ID = (msg.topic).split("ID/")[1]
        if ID == '1':
            bomba01.write(0)
            timmer = int(msg.payload)
            time.sleep(timmer)
            bomba01.write(1)
        if ID == '2':
            Lcd.setCursor(0,0)
            Lcd.clear()
            Lcd.write(" BOMBA 2 ON")
            bomba02.write(0) ## liga por um timmer
            timmer = int(msg.payload)
            time.sleep(timmer)
            bomba02.write(1) ## desliga 
            Lcd.clear()
            Lcd.write(" BOMBA 2 OFF")
            time.sleep(0.5)
    Lcd.clear()
    Lcd.write("  GARDEN ROBOT") 
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.100.15", 1883)
client.loop_forever()
