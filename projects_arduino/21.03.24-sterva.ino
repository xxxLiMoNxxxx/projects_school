#include <Servo.h>
#include <LiquidCrystal_I2C.h>

int buzzerPin = 8;
int melody[] = {440, 392, 440, 440, 392, 440, 392, 392, 440, 440, 349, 393, 349, 349, 330, 349, 330, 330, 349, 330, 349, 349, 294, 330, 294, 294, 262, 294, 262, 262, 392, 392, 392, 392, 392, 392, 392, 440, 392, 440, 440, 523, 440, 262, 262, 440, 523, 440, 440, 392, 440, 392, 392, 349, 392, 349, 349, 392, 349, 392, 392, 294};

int noteDuration = 140;

LiquidCrystal_I2C lcd(0x27,20,4);
Servo servo;

void playTone(int note, int duration) {
    tone(buzzerPin, note, duration);
    delay(duration * 1.1);
    noTone(buzzerPin);
    delay(50);
}

void playMelody() {
    for (int i = 0; i <sizeof(melody) / sizeof(melody[0]); i++) {
        playTone(melody[i], noteDuration);
    }
    delay(5000);
}

void setup() 
{
    servo.attach(11);
    lcd.init();                                  // Initialize the LCD
    lcd.backlight(); 
    lcd.setCursor(0,1); 
    lcd.print("RS6 0-MAX");                           // Turn on the backlight (if available)
    lcd.setCursor(0,2);
    pinMode(buzzerPin, OUTPUT);
}

void loop()
{
    lcd.print("0");
    delay(1000);
    servo.write(0);
    delay(750);
    lcd.clear();
    lcd.print("100");
    delay(500);
    lcd.clear();
    lcd.print("250");
    delay(350);
    lcd.clear();
    lcd.print("350");
    playMelody();
    
}