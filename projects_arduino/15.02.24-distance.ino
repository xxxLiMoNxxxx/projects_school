#include <Key.h>

int red = 13;
int yellow = 12;
int green = 11;
int trig = 6
int echo = 5
float duration;
float distance;


void setup()
{
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
}

void loop()
{
    digitalWrite(trig, LOW);
    delayMicroseconds(5);
    digitalWrite(trig, HIGH);
    delayMicroseconds(5);
    digitalWrite(red, HIGH);
    
    duration = pulseIn(echo, HIGH);
    distance = duration*0.34/2

    if (distance<=60){
        digitalWrite(red, HIGH);
        digitalWrite(yellow, LOW);
        digitalWrite(green, LOW);
    }
    else if(distance<=100){
        digitalWrite(red, HIGH);
        digitalWrite(yellow, HIGH);
        digitalWrite(green, LOW);
    }
    else if(distance<=140){
        digitalWrite(red, LOW);
        digitalWrite(yellow, LOW);
        digitalWrite(green, HIGH);
    }
    else if(distance<=160){
        digitalWrite(green, HIGH);
        delay(500);
        digitalWrite(green, LOW);
        delay(500);
        digitalWrite(green, HIGH);
        delay(500);
        digitalWrite(green, LOW);
        delay(500);
    }
    else{
        digitalWrite(red, LOW);
        digitalWrite(yellow, HIGH);
        digitalWrite(green, LOW);
    }
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
}