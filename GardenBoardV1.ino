#include <dht.h>

dht DHT;
/************************************************/
int atuador[2] = {6,7};  // rele aciona bomba de agua em linha 1 e 2  atuador 

/************************************************/
/*
 *  Sensores dht11 e umidade de solo 
 *  pinos UMIDADE DE SOLO A0, A1 , A2 ,A3 ,A4 
 *  pino dht11 - A5
*/
#define DHT11_PIN A5


int sensors_umidade[5] = {A0, A1, A2, A3, A4 };
int i=0;


/************************************************/

int STATUS_UMIDADE[5] = {0 , 0, 0, 0, 0};

String entrada;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(atuador[0], OUTPUT);
  pinMode(atuador[1], OUTPUT);
  digitalWrite(atuador[0],LOW);
  digitalWrite(atuador[1],LOW);
  
  for (i = A0; i < A5; i++){
    Serial.print("\n\tSensor de Umidade start - ");
    Serial.print(i);
    pinMode(i,INPUT);
    Serial.print("\n");    
  }

}

void loop() {
 
 entrada = Serial.readString();
 Serial.println(entrada);
 TrataString(entrada);
 
 for ( i = 0; i < 5; i++){
   STATUS_UMIDADE[i] = 0;
 }
 
  PrintSensores();
  delay(100);
  
}



void PrintSensores(){

 for (i = 0; i < 5; i++){
    STATUS_UMIDADE[i] = map(analogRead(sensors_umidade[i]),0,1023,0,100);
    //Serial.print("\t");    
  }
  
 for ( i = 0; i < 5; i++){
   Serial.print("\tA");
   Serial.print(i);
   Serial.print(" - ");
   Serial.println(STATUS_UMIDADE[i]);
   //Serial.print("\t");
    
 }

  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.print(DHT.temperature);
  Serial.print("; Humidity = ");
  Serial.println(DHT.humidity);
 
 
}

// resolver problema de contole de luminosidade 

void TrataString(String texto){
   int pin;
   int enabled;
   
   pin = texto.substring(0,1).toInt();
   enabled = texto.substring(2,3).toInt();
   bool b=(enabled ? true : false); 
   // pin           = atoi(texto.substring(0,1));
   // Enabled = atoi(texto.substring(2,3));
      
   Serial.println(pin);
   Serial.println(enabled);
   Serial.println(texto.substring(4,5));
   controle_luz(pin,b);
}

void controle_luz(int pin, bool enabled){
  digitalWrite(atuador[pin ? 1 : 0],enabled ? HIGH : LOW);
}
