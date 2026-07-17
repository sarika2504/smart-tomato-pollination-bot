#include <Servo.h>

Servo arm;

const int ENA=5;
const int IN1=6;
const int IN2=7;
const int ENB=9;
const int IN3=10;
const int IN4=11;

const int VIBRATION=8;
const int SERVO_PIN=3;

void setup(){
Serial.begin(9600);

pinMode(ENA,OUTPUT);
pinMode(IN1,OUTPUT);
pinMode(IN2,OUTPUT);
pinMode(ENB,OUTPUT);
pinMode(IN3,OUTPUT);
pinMode(IN4,OUTPUT);

pinMode(VIBRATION,OUTPUT);

arm.attach(SERVO_PIN);
arm.write(90);
}

void loop(){

if(Serial.available()){

char cmd=Serial.read();

switch(cmd){

case 'F':
forward();
break;

case 'B':
backward();
break;

case 'L':
left();
break;

case 'R':
right();
break;

case 'S':
stopRobot();
break;

case 'P':
pollinate();
break;

}

}

}

void forward(){
digitalWrite(IN1,HIGH);
digitalWrite(IN2,LOW);
digitalWrite(IN3,HIGH);
digitalWrite(IN4,LOW);
analogWrite(ENA,180);
analogWrite(ENB,180);
}

void backward(){
digitalWrite(IN1,LOW);
digitalWrite(IN2,HIGH);
digitalWrite(IN3,LOW);
digitalWrite(IN4,HIGH);
analogWrite(ENA,180);
analogWrite(ENB,180);
}

void left(){
digitalWrite(IN1,LOW);
digitalWrite(IN2,HIGH);
digitalWrite(IN3,HIGH);
digitalWrite(IN4,LOW);
analogWrite(ENA,180);
analogWrite(ENB,180);
}

void right(){
digitalWrite(IN1,HIGH);
digitalWrite(IN2,LOW);
digitalWrite(IN3,LOW);
digitalWrite(IN4,HIGH);
analogWrite(ENA,180);
analogWrite(ENB,180);
}

void stopRobot(){
analogWrite(ENA,0);
analogWrite(ENB,0);
}

void pollinate(){

stopRobot();

arm.write(45);
delay(800);

digitalWrite(VIBRATION,HIGH);
delay(2000);
digitalWrite(VIBRATION,LOW);

arm.write(90);
delay(800);

}
