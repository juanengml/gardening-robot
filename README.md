# Machine Learning Engineer Nanodegree
## Projeto: Gardening Robot 

### INSTALL DATA_SCIENCE

Este projeto requer **Python2.7** com as bibliotecas a baixo
- [Numpy](https://www.numpy.org/)
- [Scikit-learn](http://scikit-learn.org/stable/)
- [Pandas](http://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [matplotlib](http://matplotlib.org/)

### INSTALL IOT_IDE

Este projeto requer **arduino-IDE** com as bibliotecas a baixo
PS: para instalar as boards esp8266/nodemcu 
ARDUINO IDE = >
Abra File => 
DPS Preferences => Cole isso na barra de
"URLS ADICIONAIS PARA GERENCIAMENTO DE PLACAS "
 http://arduino.esp8266.com/stable/package_esp8266com_index.json

- [String.h](https://www.arduino.cc/reference/en/language/variables/data-types/stringobject/)
- [ESP8266Wifi.h](http://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/readme.html)
- [PubSubClient.h](https://pubsubclient.knolleary.net/api.html)

### PRÊ-RUN 
Neste projeto usei 4 nodemcu, 4 sensores de solo, cada 
um com um codigo de coleta apenas auterando apenas ID
do IoT.

### RUN OFICIAL
```bash
$ jupyter notebook Gardening Robot.ipynb
```

### DADOS
Os dados coletados neste dataset são 5405, com 5 caracteristicas especificas 
ID, MES, DIA, Hora, umidade.

**CARACTERISTICAS**
1. ``ID``: Nivel de umidade,1 = arido , 2 = seco, 3 = umido, 4 = molhado 
2. ``MES``: Mes que foi gravado o dado.
3. ``DIA``: dia que foi gravado os dado
4. ``Hora``: Hora que foi gravado o dado

**TARGET**

5. ``umidade``: Leitura dos Sensores de Umidade de Solo.

### ABOUT
O robo deve analisar os dados dos sensores de umidade de solo e classificar 
os em niveis de ``arido``,``seco``,``umido``,``molhado``, ele 
usa KNN, para classificar e gerar predição de novos dados.
há magia esta na predição, pois ela mostra os status atual de um novo sensor para uma nova leitura.


