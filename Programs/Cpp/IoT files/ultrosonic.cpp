int inches = 0;
int cm = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
    pinMode(triggerPin, OUTPUT);
    digitalWrite(triggerPin, LOW);
    delayMicroseconds(2);
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin, LOW);
    pinMode(echoPin, INPUT);
    return pulseIn(echoPin, HIGH);
}

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    cm = 0.01723*readUltrasonicDistance(8,8);
    inches = (cm/2.54);
    Serial.print(inches);
    Serial.print("in,");
    delay(100);
}