#include <String.h>

long Humidade;
long day;
long mes;
long hora;
long data;

void setup(){
  Serial.begin(115200);

  // Se o pino de entrada analógica 0 é deixado desconectado,
  // o ruído aleatório analógico irá causar a chamada de randomSeed()
  //  gerar sementes aleatórias diferentes cada vez que o sketch roda.
  // randomSeed() basicamente "embaralha" a função random().
  randomSeed(analogRead(0));
}

void loop() {
  char getData[100];
  strcpy(getData,PegarDado());  
  Serial.println(getData);
  delay(50);
  
}

char* PegarDado(){
  long ID  = 01;  /// change ID DO IOT 
  day = random(30);
  mes = random(12);
  hora = random(59);
  Humidade = random(100);
  static char data[100];
  sprintf(data, "ID: %lu; MES: %lu; DIA: %lu; Hora: %lu; Humidade: %lu", ID, mes, day,hora,Humidade);
  return data;
}

