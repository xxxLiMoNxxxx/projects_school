#include <Key.h>

int red = 13;
int yellow = 12;
int green = 11;


void setup()
{
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
}

void loop()
{
    digitalWrite(red, HIGH);
    delay(2000);
    digitalWrite(yellow, HIGH);
    delay(1000);
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, HIGH);
    delay(500);
    digitalWrite(green, LOW);
    delay(500);
    digitalWrite(green, HIGH);
    delay(500);
    digitalWrite(green, LOW);
    delay(500);
    digitalWrite(green, HIGH);
    digitalWrite(yellow, HIGH);
    digitalWrite(green, LOW);
    delay(1000);
    digitalWrite(yellow, LOW);
}