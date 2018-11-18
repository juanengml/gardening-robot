import matplotlib.pyplot as plt


def grafico_linha(lista):
 plt.plot( lista )
 plt.savefig('graph.jpg')
 print "Grafico gerado "

grafico_linha(range(0,100))

