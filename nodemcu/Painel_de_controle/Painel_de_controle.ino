// Libs
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Vars
const char* SSID = "tapodi"; // rede wifi
const char* PASSWORD = "naolembro"; // senha da rede wifi

const char* BROKER_MQTT = "192.168.100.3"; // ip/host do broker
int BROKER_PORT = 1883; // porta do broker

// prototypes
void initPins();
void initSerial();
void initWiFi();
void initMQTT();

WiFiClient espClient;
PubSubClient MQTT(espClient); // instancia o mqtt

// setup
void setup() {
  initPins();
  initSerial();
  initWiFi();
  initMQTT();
}

void loop() {
  if (!MQTT.connected()) {
    reconnectMQTT();
  }
  recconectWiFi();
  MQTT.loop();
}

// implementacao dos prototypes

void initPins() {
  pinMode(D7, OUTPUT);
  
  digitalWrite(D7, 0);
}

void initSerial() {
  Serial.begin(115200);
}
void initWiFi() {
  delay(10);
  Serial.println("Conectando-se em: " + String(SSID));

  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Conectado na Rede " + String(SSID) + " | IP => ");
  Serial.println(WiFi.localIP());
}

// Funcão para se conectar ao Broker MQTT
void initMQTT() {
  MQTT.setServer(BROKER_MQTT, BROKER_PORT);
  MQTT.setCallback(mqtt_callback);
}

//Função que recebe as mensagens publicadas
void mqtt_callback(char* topic, byte* payload, unsigned int length) {

  String message;
  for (int i = 0; i < length; i++) {
    char c = (char)payload[i];
    message += c;
  }
  Serial.println("Tópico => " + String(topic) + " | Valor => " + String(message));
  ledControl(message[0]);

  Serial.flush();
}

void reconnectMQTT() {
  while (!MQTT.connected()) {
    Serial.println("Tentando se conectar ao Broker MQTT: " + String(BROKER_MQTT));
    if (MQTT.connect("ESP8266-ESP12-E")) {
      Serial.println("Conectado");
      MQTT.subscribe("/garden/painel/");
      MQTT.publish("/garden/painel/","UP");

    } else {
      Serial.println("Falha ao Reconectar");
      Serial.println("Tentando se reconectar em 2 segundos");
      delay(2000);
    }
  }
}

void recconectWiFi() {
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
}







void ledControl(char cmd){
  
  switch(cmd){
    case 'q': digitalWrite(D8,HIGH);  break; 
    case 'w': digitalWrite(D8,LOW);   break;

    case 'e': digitalWrite(D7,HIGH);  break;
    case 'r': digitalWrite(D7,LOW);   break;
    
    case 't': digitalWrite(D6,HIGH);  break;
    case 'y': digitalWrite(D6,LOW);   break;
     
    case 'u': digitalWrite(D5,HIGH); break;
    case 'i': digitalWrite(D5,LOW);  break;

    case 'o': digitalWrite(D4,HIGH); break;
    case 'a': digitalWrite(D4,LOW); break;
    
    case 'd': digitalWrite(D3,HIGH); break;
    case 'f': digitalWrite(D3,LOW); break;

    case 'g': digitalWrite(D2,HIGH); break;
    case 'h': digitalWrite(D2,LOW); break;
     
    break;
  }

}





