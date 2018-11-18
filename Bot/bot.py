# -*- coding: utf-8 -*-

import time
import telepot
from telepot.loop import MessageLoop
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


std = """Sou um Robo desenvolvido para analisar sensor de umidade de solo, classificar niveis de umidade e prever se as plantas no jardim/horta precisa ser ragada ou não, no que posso ajudar ? """


def grafico_linha():
 df = pd.read_csv("../mqtt/test/log.csv")
 sns.pairplot(df)
 sns_plot = sns.pairplot(df)
 umidade = df[df.columns[4:]] 
 plot = umidade.plot()
 fig = plot.get_figure()
#  fig.savefig("output.png")
 fig.savefig('graph.jpg')
 sns_plot.savefig("output.png")
 print "Grafico gerado "


def sensores():
 df = pd.read_csv("../mqtt/test/log.csv")
 lista = []
 tamanho = len(df)
 for p in range(2):
  dado = (np.array(df[tamanho-1:tamanho]).tolist())[0]
  n_dado = "\t * IoT: Umidade\nID: %s \nMes: %s\nDia: %s\nHora: %s\nNivel: %s" % (dado[0],dado[1],dado[2],dado[3],dado[4])
  lista.append(n_dado)
 return lista
 

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == 'text':
    	print msg['text']
    	if msg['text'] == "Oi":
          bot.sendMessage(chat_id, std)
        if msg['text'] == "/status":
          bot.sendMessage(chat_id, "Buscando dado no banco....")
          dados = sensores()
          for p in range(len(dados)):
          	bot.sendMessage(chat_id, dados[p])
    if msg['text'] == "/graph":    
        grafico_linha()      	
        bot.sendMessage(chat_id, "Gerando grafico de ploter...")
        bot.sendPhoto(chat_id, open('graph.jpg', 'rb'))
        bot.sendMessage(chat_id, "Gerando grif graph...")
        bot.sendPhoto(chat_id, open('output.png', 'rb'))

       


#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot('TOKEEEEEEEEEEEEEEEEENNNNNNNNN')
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

