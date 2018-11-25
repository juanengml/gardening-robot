# -*- coding: utf-8 -*-

import time
import telepot
from telepot.loop import MessageLoop
import numpy as np
import panda as pd
import matplotlib.pyplot as plt
#import seaborn as sns


std = """Sou um Robo desenvolvido para analisar sensor de umidade de solo, classificar niveis de umidade e prever se as plantas no jardim/horta precisa ser ragada ou não, no que posso ajudar ? """

def query_20(ID,p):
    df = pd.read_csv("../mqtt/test/log.csv")
    query = df.iloc[len(df)-p:len(df)]
    ID = (query['ID'] == ID).tolist()
    return query[ID]

def grafico_linha():
 df = pd.read_csv("../mqtt/test/log.csv")
 umidade = df[df.columns[4:]] 
 plot = umidade.plot()
 fig = plot.get_figure()
#  fig.savefig("output.png")
 fig.savefig('graph.jpg')
 print "Grafico gerado "


def sensores():
 lista = []
 df = pd.read_csv("../mqtt/test/log.csv")
 tamanho = len(df)
 dado = (np.array(df[tamanho-5:tamanho]).tolist())
 n_dado = []
 for i in range(len(dado)):
    #for j in range(len(dado[i])):     
        n_dado = "IoT ID: %s\nMES: %s\nDIA: %s\nHora: %s\nUmidade: %s\n*************" % (dado[i][0],dado[i][1],dado[i][2],dado[i][3],dado[i][4])
        lista.append(n_dado)
 #print lista
 return lista
 

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == 'text':
    	print msg['text']
    	if msg['text'] == "Oi":
          bot.sendMessage(chat_id, std)
          #bot.sendMessage(chat_id, "this is sample [text](www.test.com)",parse_mode= 'Markdown')
        if msg['text'] == "/status":
          bot.sendMessage(chat_id, "Buscando dado no banco....")
          dados = sensores()
          for p in range(len(dados)):
          	bot.sendMessage(chat_id, dados[p])
    if msg['text'] == "/graph":    
        grafico_linha()      	
        bot.sendMessage(chat_id, "Gerando grafico de ploter...")
        bot.sendPhoto(chat_id, open('graph.jpg', 'rb'))
#        bot.sendMessage(chat_id, "Gerando grid graph...")
#        bot.sendPhoto(chat_id, open('output.png', 'rb'))
    if msg['text'] == "/cmds":    
    	dado = msg['text']
    	bot.sendMessage(chat_id, "Para usar o comando /query use o exemplo abaixo\n/query id:02\n/query all\n/query id:03 range:100\nCom isso o sistema fara uma busca pelo ID do sensor, ou mostrara todos os sensores conectados e os seus respctivos niveis, o range definira a faixa que ele vai buscar")
            
    if "/query" in msg['text']:    
    	dado = msg['text']
        #print dado.split(":")[0], 
        sensor = int(dado.split(":")[1])
        r =  query_20(sensor,100).values
        for p in range(len(r)):
           #bot.sendMessage(chat_id, "IoT %s | Data: %s/%s/2018 | hora: %s\nUmidade: %s" % list(r[p])[0],list(r[p])[1],list(r[p])[2],list(r[p])[3],list(r[p])[4])
    	    bot.sendMessage(chat_id,"%s" % list(r[p]))


       


#TOKEN = sys.argv[1]  # get token from command-line


 
bot = telepot.Bot('720770185:AAEQeCMNxPA6WIn-zWMehXFTXI14jdGg3uA')

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

