#include <Stepper.h>

// # steps for full 360-degree rotation, change to fit your motor
int stepsPerRevolution = 2048;
int rpm = 10;
// set a speed for the stepper motor

int penpin = 6;
int penpin2 = 7;

// Important positions for the Printer
int MaxY = (stepsPerRevolution * 7) / 100;
int MaxX = (stepsPerRevolution * 6) / 100;

int CurrentX = 0;
int CurrentY = 0;



// initialize stepper library on pins 8 - 11
// pin order IN1, IN3, IN2, IN4
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);
Stepper myStepper2(stepsPerRevolution, 2, 3, 4, 5);


void setup() {
  pinMode(penpin, OUTPUT);
  pinMode(penpin2, OUTPUT);


  myStepper.setSpeed(rpm);
  myStepper2.setSpeed(rpm);
  Serial.begin(9600);
}


void loop() {
  digitalWrite(penpin, HIGH);
  digitalWrite(penpin2, HIGH);
  if (Serial.available() > 0) {

    String msg = Serial.readString();

    if (msg.indexOf(",") != -1) {
      String X = msg.substring(0, msg.indexOf(','));    // "X"
      String Y = msg.substring(msg.indexOf(',') + 1);  // "Y"
      int IntY = Y.toInt();
      int IntX = X.toInt();
      int MoveY = MaxY * IntY;
      int MoveX = MaxX * IntX;
      myStepper2.step(MoveX);
      myStepper.step(MoveY);

    }
    

    if (msg == "ZEROPOINT") {
      myStepper2.step(stepsPerRevolution * 7);
      myStepper.step(stepsPerRevolution * 6);
    } else if (msg == "MAXPOINT") {
      myStepper2.step(-stepsPerRevolution * 7);
      myStepper.step(-stepsPerRevolution * 6);
    } else if (msg == "HALF") {
      int Half = MaxY * 50;
      int HalfX = MaxX * 50;
      myStepper2.step(-Half);
      myStepper.step(-HalfX);
      CurrentX = 50;
      CurrentY = 50;

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