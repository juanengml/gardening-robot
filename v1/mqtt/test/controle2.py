import pyupm_i2clcd as lcd  # importa biblioteca para i2c 
import mraa
import time                
import paho.mqtt.client as mqtt

TOPIC = "/garden/painel/#"

Lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
Lcd.clear() 
Lcd.setColor(0, 0, 255) 
reset = mraa.Gpio(6)        
bomba01 = mraa.Gpio(2)        
bomba02 = mraa.Gpio(3)        
 

reset.dir(mraa.DIR_OUT)   
bomba01.dir(mraa.DIR_OUT)   
bomba02.dir(mraa.DIR_OUT)   

def msg(sensor,status):
    Lcd.clear()
    Lcd.setCursor(0,0)
    Lcd.write(sensor)
    Lcd.setCursor(1,0)
    Lcd.write(status)

def on_connect(self,client, data, rc):
    self.subscribe([(TOPIC,0)])

def on_message(client, userdata, msg):
    print "TOPICO: ",msg.topic," payload: ",str(msg.payload)
    #client.publish("/garden/painel/reset/status/", '1')
    #client.publish("/garden/painel/bombas/ID/"+menu, entrada)
    if "/garden/painel/reset/status/" == msg.topic:
        if msg.payload == '1':
          reset.write(1)
        else:  
          reset.write(0)    
    if "/garden/painel/bombas/ID/" in msg.topic:
        print (msg.topic).split("ID/")[1],msg.payload+"s"
        ID = (msg.topic).split("ID/")[1]
        if ID == '1':
            bomba01.write(1)
            timmer = int(msg.payload)
            time.sleep(timmer)
            bomba01.write(0)
        if ID == '2':
            bomba02.write(1)
            timmer = int(msg.payload)
            time.sleep(timmer)
            bomba02.write(0)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.100.3", 1883)
client.loop_forever()
