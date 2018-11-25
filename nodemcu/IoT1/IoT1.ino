#include <string.h>
#include <ESP8266WiFi.h>  //essa biblioteca já vem com a IDE. Portanto, não é preciso baixar nenhuma biblioteca adicional
#include <PubSubClient.h> // Importa a Biblioteca PubSubClient


WiFiClient clientMQTT;
WiFiClient client;
long ultimo_envio;
PubSubClient MQTT(clientMQTT); // Instancia o Cliente MQTT passando o objeto clientMQTT
float umidade;

#define SSID_REDE     "tapodi"    // nome da rede 
#define SENHA_REDE    "naolembro"        // senha da rede 
#define IP_BROKER     "192.168.100.13"       // IP DO BROKER LOCAL
#define TOPICO         "home/gardem/horta/planta/02" //  PLANTA 01  

void setup(){
  Serial.begin(115200);
  initWiFi();
  initMQTT();
  ultimo_envio = 0;
  
}

void loop() {
 
 char getData[100];
  strcpy(getData,PegarDado());  
 
  delay(50);
  ////////////////
  VerificaConexoesWiFIEMQTT(); 
  
if(!client.connected())
    {
        VerificaConexoesWiFIEMQTT(); 
    }
 
    //verifica se é o momento de enviar informações via MQTT
    if ((millis() - ultimo_envio) > 100)
    {
        
        MQTT.publish(TOPICO, getData);
         ultimo_envio = millis();
    }
    
    delay(100);
  
}

void initWiFi() 
{
    delay(10);
    Serial.println("------Conexao WI-FI------");
    Serial.print("Conectando-se na rede: ");
    Serial.println("qual e a senha");
    Serial.println("Aguarde");
     
    reconectWiFi();
}


void initMQTT() 
{
    MQTT.setServer(IP_BROKER, 1883);   //informa qual broker e porta deve ser conectado
    MQTT.setCallback(mqtt_callback);            //atribui função de callback (função chamada quando qualquer informação de um dos tópicos subescritos chega)
}

void mqtt_callback(char* topic, byte* payload, unsigned int length) 
{
        
}




void reconectWiFi() 
{
    if (WiFi.status() == WL_CONNECTED)
        return;
         
    WiFi.begin(SSID_REDE, SENHA_REDE); // Conecta na rede WI-FI
     
    while (WiFi.status() != WL_CONNECTED) 
    {
        delay(100);
        Serial.print(".");
    }
   
    Serial.println();
    Serial.print("Conectado com sucesso na rede ");
    Serial.print("qual e a senha");
    Serial.println("IP obtido: ");
    Serial.println(WiFi.localIP());
}

void reconnectMQTT() 
{
    while (!MQTT.connected()) 
    {
        Serial.print("* Tentando se conectar ao Broker MQTT: ");
        Serial.println(IP_BROKER);
        if (MQTT.connect("IoT:02")) 
        {
            Serial.println("Conectado com sucesso ao broker MQTT!");
            MQTT.subscribe("IoT: 02 ONLINE"); 
        } 
        else
        {
            Serial.println("Falha ao reconectar no broker.");
            Serial.println("Havera nova tentatica de conexao em 2s");
            delay(2000);
        }
    }
}

void VerificaConexoesWiFIEMQTT(void)
{
    if (!MQTT.connected()) 
        reconnectMQTT(); //se não há conexão com o Broker, a conexão é refeita
     
     reconectWiFi(); //se não há conexão com o WiFI, a conexão é refeita
}



 
char* PegarDado(){
  
  int ValorADC;
  float UmidadePercentual;
  ValorADC = analogRead(0);   //418 -> 1.0V
  UmidadePercentual = 100 * ((418-(float)ValorADC) / 418);

  long ID = 02;  /// change ID DO IOT 
  umidade = UmidadePercentual;
  static char data[100];
  Serial.println(umidade);
  
  sprintf(data, "ID: %lu; umidade: %.2f", ID,umidade);
  Serial.println(data);
  return data;
}
