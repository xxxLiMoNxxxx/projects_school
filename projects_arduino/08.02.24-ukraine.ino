#include <Key.h>

int first_ukraine = 13;
int second_ukraine = 12;
int third_ukraine = 11;


void setup()
{
    pinMode(first_ukraine, OUTPUT);
    pinMode(second_ukraine, OUTPUT);
}

void loop()
{
    //1
    digitalWrite(first_ukraine, HIGH);
    delay(500);
    digitalWrite(first_ukraine, LOW);
    delay(500);
    digitalWrite(second_ukraine, HIGH);
    delay(500);
    digitalWrite(second_ukraine, LOW);
    delay(1500);
    //2
    digitalWrite(first_ukraine, HIGH);
    delay(500);
    digitalWrite(second_ukraine, HIGH);
    delay(500);
    digitalWrite(first_ukraine, LOW);
    delay(500);
    digitalWrite(second_ukraine, LOW);
    delay(1500);
    //3
    digitalWrite(first_ukraine, HIGH);
    delay(250);
    digitalWrite(second_ukraine, HIGH);
    delay(500);
    digitalWrite(first_ukraine, LOW);
    delay(250);
    digitalWrite(second_ukraine, LOW);
    delay(1500);
}