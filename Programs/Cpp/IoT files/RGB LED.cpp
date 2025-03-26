int redPin = 10;
int greenpin = 9;
int bluepin = 8;

void setup()
{
	pinMode (redPin , OUTPUT);
	pinMode (greenpin, OUTPUT);
	pinMode (bluepin, OUTPUT);
}

void loop()
{
	setColor(225, 0, 0);
	delay(1000); 
	setColor(0, 225, 0);
	delay(1000); 
	setColor(0, 0, 225);
	delay(1000); 
	setColor(225, 225, 225);
	delay(1000); 
	setColor(170, 0, 225);
	delay(1000); 
}

void  setColor(int redValue, int greenValue, int blueValue)
{
	analogWrite(redPin, redValue);
	analogWrite(greenpin, greenValue);
	analogWrite(bluepin, blueValue);
}