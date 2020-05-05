void setup() {
 pinMode(8, OUTPUT); //Sygnały sterujące kierunkiem obrotów silnika nr 1
 pinMode(9, OUTPUT);


pinMode(10, OUTPUT); //Sygnały sterujące kierunkiem obrotów silnika nr 2
 pinMode(11, OUTPUT);
}

void loop() {
  digitalWrite(8, LOW); //Silnik nr 1 - obroty w lewo
  digitalWrite(9, HIGH); 
  digitalWrite(10, LOW); //Silnik nr 2 - obroty w lewo
  digitalWrite(11, HIGH); 
  delay(5000);
  
  digitalWrite(8, HIGH); //Silnik nr 1 - obroty w prawo
  digitalWrite(9, LOW); 
  digitalWrite(10, HIGH); //Silnik nr 2 - obroty w prawo
  digitalWrite(11, LOW); 
  delay(5000);  
}
