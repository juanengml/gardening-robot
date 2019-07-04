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
#define DHT11_PIN A6

unsigned long lastSend;

int sensors_umidade[6] = {A0, A1, A2, A3, A4,A5 };
int i=0;


/************************************************/

int STATUS_UMIDADE[6] = {0 , 0, 0, 0, 0 , 0};

char entrada;

void setup() {
  // put your setup code here, to run once:
  lastSend = 0;

  Serial.begin(9600);
  pinMode(atuador[0], OUTPUT);
  pinMode(atuador[1], OUTPUT);
  digitalWrite(atuador[0],LOW);
  digitalWrite(atuador[1],LOW);
  
  for (i = A0; i < A6; i++){
  //  Serial.print("\n\tSensor de Umidade start - ");
  //  Serial.print(i);
    pinMode(i,INPUT);
  //  Serial.print("\n");    
  }

}

void loop() {


 if(Serial.available())
   {
     entrada = Serial.read();
     Serial.print(entrada);
     Serial.print("\n");
     controle_luz(entrada);
   }
 
 
 for ( i = 0; i < 5; i++){
   STATUS_UMIDADE[i] = 0;
 }
 
  PrintSensores();
  delay(1000);
  
}



void PrintSensores(){

 for (i = 0; i < 6; i++){
    STATUS_UMIDADE[i] = map(analogRead(sensors_umidade[i]),0,1023,100,0);
    //Serial.print("\t");    
  }
 
 
 if ( millis() - lastSend > 2000 ) { // Update and send only after 1 seconds
     Serial.print("{'");
    int chk = DHT.read11(DHT11_PIN);
    Serial.print("Temperature': ");
    Serial.print(DHT.temperature);
    Serial.print(", 'Humidity': ");
    Serial.print(DHT.humidity);
//    Serial.println('}');
    
//    Serial.print("{"); 
    
    for ( i = 0; i < 6; i++){
       Serial.print("'Solo-");
       Serial.print(i);
       Serial.print("':");
       Serial.print(STATUS_UMIDADE[i]);
       if (i == 5)
        Serial.print(" ");
       else{
        Serial.print(", ");
        } 
        
     }
     Serial.println("}");
    lastSend = millis();
  }
 
 
}


// resolver problema de contole de luminosidade 


void controle_luz(char letra){
  switch(letra){
    case 'q':
       digitalWrite(atuador[0],HIGH);
    break;       
    case 'w':
       digitalWrite(atuador[0],LOW);
    break;
    case 'e':
       digitalWrite(atuador[1],HIGH);
    break;
    case 'r':
       digitalWrite(atuador[1],LOW);
    break;
  }
  
}
