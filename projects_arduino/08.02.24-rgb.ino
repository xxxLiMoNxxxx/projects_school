#include <Key.h>

int red = 11;
int green = 10;
int blue = 9;


void setup()
{
    pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(blue, OUTPUT);
}

void loop()
{
    analogWrite(red, 252);
    analogWrite(green, 3);
    analogWrite(blue, 207);
    delay(1000);
    analogWrite(red, 32);
    analogWrite(green, 3);
    analogWrite(blue, 252);
    delay(1000);
    analogWrite(red, 252);
    analogWrite(green, 161);
    analogWrite(blue, 3);
    delay(1000);
    analogWrite(red, 255);
    analogWrite(green, 127);
    analogWrite(blue, 80);
    delay(1000);
    analogWrite(red, 197);
    analogWrite(green, 130);
    analogWrite(blue, 217);
    delay(1000);
    analogWrite(red, 148);
    analogWrite(green, 96);
    analogWrite(blue, 163);
    delay(1000);
    analogWrite(red, 63);
    analogWrite(green, 2);
    analogWrite(blue, 82);
    delay(1000);
    analogWrite(red, 255);
    analogWrite(green, 0);
    analogWrite(blue, 144);
    delay(1000);
    analogWrite(red, 0);
    analogWrite(green, 0);
    analogWrite(blue, 0);
    delay(1000);
}