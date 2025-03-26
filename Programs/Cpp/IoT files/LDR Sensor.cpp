void setup()
{
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop()
{
  int sensorread = analogRead(A0);
  Serial.print("LDR     value.");
  Serial.println(sensorread);
  delay(500);
}