const int pushbutton = 2;

void setup()
{
	pinMode(10, OUTPUT);
	pinMode(pushbutton, INPUT);
}

void loop()
{
	int inputval=digitalRead(pushbutton);
	if(inputval==1){
		digitalWrite(10,HIGH);
	}
	if(inputval==0){
		digitalWrite(10,LOW);
	}
}
