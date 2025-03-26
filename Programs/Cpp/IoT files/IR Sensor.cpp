void setup()
{
    pinMode(2, INPUT);
    Serial.begin(9600);
}

void loop()
{
    IR = digitalRead(2);
    Serial.println(IR);
    delay(10);
    
}