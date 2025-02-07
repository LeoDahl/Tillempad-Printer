/**
  File: Arduino.cpp
  Author: Leo Dahl
  Date: 2025-02-07
  Description: This code works as a main gateway between the computer and Arduino
  The code listens for Serial information and moves two stepper motors
*/

#include <Stepper.h>

int stepsPerRevolution = 2048;  // How many steps in a 360 rotation
int rpm = 10;                   // set a speed for the stepper motor

int penpin = 6;
int penpin2 = 7;

// Important positions for the Printer
int oneStepY = (stepsPerRevolution * 7) / 100;
int oneStepX = (stepsPerRevolution * 6) / 100;

int CurrentX = 0;
int CurrentY = 0;

// Structure for how much the servos should move. This value is changed and returned by Calculate_Message function
struct Result {
  int MoveX;
  int MoveY;
};

// initialize stepper library on pins 8 - 11
// pin order IN1, IN3, IN2, IN4
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
Stepper myStepper2(stepsPerRevolution, 2, 3, 4, 5);


void setup() {

  // Set speed to both Steppers by RPM variable
  myStepper.setSpeed(rpm);
  myStepper2.setSpeed(rpm);
  Serial.begin(9600);
}


void loop() {
  if (Serial.available() > 0) {  // Check if serial information has been sent

    String msg = Serial.readString(); // serial information as string

    if (msg.indexOf(",") != -1) { // Check if msg has symbol ","
      Result Coords = Calculate_Message(msg);
      int MoveX = Coords.MoveX;
      int MoveY = Coords.MoveY;
      myStepper2.step(MoveX); 
      myStepper.step(MoveY); 
    }


    // Preset commands
    } else if (msg == "UP") {
      myStepper2.step(-stepsPerRevolution);
    } else if (msg == "DOWN") {
      myStepper2.step(stepsPerRevolution);
    } else if (msg == "LEFT") {
      myStepper.step(stepsPerRevolution);
    } else if (msg == "RIGHT") {
      myStepper.step(-stepsPerRevolution);
    } else if (msg == "PEN") {
      digitalWrite(penpin, LOW);
      delay(100);
    }
  }
}
/*
  Splits string by symbol "," and converts one string value to X and Y int values.
  Parameters:
    - String: "X,Y"
  Returns: 
    - New values of Struct result
*/
Result Calculate_Message(String msg) {

  String X = msg.substring(0, msg.indexOf(','));   // "X"
  String Y = msg.substring(msg.indexOf(',') + 1);  // "Y"
  int IntY = Y.toInt();
  int IntX = X.toInt();
  int MoveY = oneStepY * IntY;
  int MoveX = oneStepX * IntX;

  Result r;
  r.MoveX = MoveX;
  r.MoveY = MoveY;
  return r;
}