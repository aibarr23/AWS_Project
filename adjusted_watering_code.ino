
#include <Arduino.h>
#include <stdbool.h>
// Attach the serial display's RX line to digital pin 2
Uart mySerial (&sercom0, 13, 8, SERCOM_RX_PAD_1, UART_TX_PAD_0);


// Here we are setting up some water thersholds that we will 
// use later. Note that you will need to change these to match
// your soil type and environment. 

/********************************************************
 * Change these values based on your calibration values
 *******************************************************/
int thresholdUp = 400;
int thresholdDown = 250;

// We are setting up the pin A0 on the redboard to be our sensor
// pin input:
int solenoidPin = 10;
int solenoidPin1 = 11;
int solenoidPin2 = 12;
int solenoidPin3 = A3;
int soilPin = A0;
int soilPin1 = A1;
int soilPin2 = A2;
int soilPower = 7;
int soilPower1 = 8;
int soilPower2 = 9;  

boolean solenoidControl0 == False; // user is not controlling solenoid0
boolean solenoidControl1 == False; // user is not controlling solenoid1
boolean solenoidControl2 == False; // user is not controlling solenoid2
boolean solenoidControlOpen0 == False; // solenoid0 is not open
boolean solenoidControlOpen1 == False; // solenoid1 is not open
boolean solenoidControlOpen2 == False; // solenoid2 is not open
boolean returnControl == False; // microcontroller is currently in control of solenoids
boolean closeAll == False; // closing all solenoids is currently false

void setup(){
  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(soilPower, OUTPUT);//Set D7 as an OUTPUT
  digitalWrite(soilPower, LOW);//Set to LOW so no power is flowing through the sensor

  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(soilPower1, OUTPUT);//Set D8 as an OUTPUT
  digitalWrite(soilPower1, LOW);//Set to LOW so no power is flowing through the sensor
    
  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(soilPower2, OUTPUT);//Set D9 as an OUTPUT
  digitalWrite(soilPower2, LOW);//Set to LOW so no power is flowing through the sensor

  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(solenoidPin, OUTPUT);//Set D10 as an OUTPUT
  digitalWrite(solenoidPin, LOW);//Set to LOW so no power is flowing through the sensor

  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(solenoidPin1, OUTPUT);//Set D11 as an OUTPUT
  digitalWrite(solenoidPin1, LOW);//Set to LOW so no power is flowing through the sensor

  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(solenoidPin2, OUTPUT);//Set D12 as an OUTPUT
  digitalWrite(solenoidPin2, LOW);//Set to LOW so no power is flowing through the sensor
}


void loop() {

  int sensorValue;
  sensorValue = readSoil();

  int sensorValue1;
  sensorValue1 = readSoil1();

  int sensorValue2;
  sensorValue2 = readSoil2();
  
  if (returnControl == True) { //user returns control to solenoids
    solenoidControl0 = False; // user is not controlling solenoid0
    solenoidControl1 = False; // user is not controlling solenoid1   
    solenoidControl2 = False; // user is not controlling solenoid2
  }
  
  if (solenoidControl0 == False) {
    int wateringPot(sensorValue, solenoidPin);
  }
  if (solenoidControl1 == False) {
    int wateringPot(sensorValue1, solenoidPin1);
  }
  if (solenoidControl2 == False) {
    int wateringPot(sensorValue2, solenoidPin2);
  }
}

int wateringPot (int sensorvalue, int solenoidPin) { //what do i refer to high/low as?
    
  if (sensorValue <= thresholdDown) {
    //water it
    digitalWrite(solenoidPin, HIGH); //open solenoid
    delay(61000); //wait a minute and a second 
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      delay(60000); //wait a minute
      digitalWrite(solenoidPin, LOW); //close solenoid
      delay(1000);
    }
    else {
      digitalWrite(solenoidPin, LOW); //close solenoid
      delay(1000);
    }
  }
  else if (sensorValue >= thresholdUp) {
    //wait and check later 
    delay(36000000); //wait an hour
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      digitalWrite(solenoidPin, HIGH); //open solenoid
      delay(61000); //wait a minute and a second 
      sensorValue = readSoil();
      if (sensorValue <= thresholdDown) {
        delay(60000); //wait a minute
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
      else {
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
    }
  }
  else {
    delay(18000000); //wait 30 min 
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      digitalWrite(solenoidPin, HIGH); //open solenoid
      delay(61000); //wait a minute and a second 
      sensorValue = readSoil();
      if (sensorValue <= thresholdDown) {
        delay(60000); //wait a minute
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
      else {
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
    }
  }
}

void solenoids(bool solenoidControl, bool solenoidControlopenclose, int So) {

  int solenoids = [0, 10, 11. 12];

  if (solenoids[So] == 0) { //closing all solenoids, microcontrller is still not in control
    digitalWrite(solenoidPin, HIGH);
    digitalWrite(solenoidPin1, HIGH);
    digitalWrite(solenoidPin2, HIGH);
  }
  else{
    if (solenoidControl == True) { //user interacts with solenoid0 switch
      if (solenoidControlopenclose == True) { //user opens solenoid
        digitalWrite(solenoids[So], HIGH);
      }
      else if (solenoidcontrol == False){ //close solenoid when it is open
        digitalWrite(solenoids[So], LOW);
      }
    }
  }
  
  
}  

int readSoil()
{
    digitalWrite(soilPower, HIGH);//turn D7 "On"
    delay(10);//wait 10 milliseconds 
    int val = analogRead(soilPin);//Read the SIG value form sensor 
    digitalWrite(soilPower, LOW);//turn D7 "Off"
    return val;//send current moisture value
}

int readSoil1()
{
  digitalWrite(soilPower1, HIGH); // turn d8 on 
  delay(10); //wait 10 milliseconds
  int val1 = analogRead(soilPin1); //Read the SIG value from sensor 2
  digitalWrite(soilPower1, LOW); // turn D8 off
  return val1; //send current moisture value 
}
int readSoil2()
{
  digitalWrite(soilPower2, HIGH); // TURN D9 on 
  delay(10); // wait 10 milliseconds 
  int val2 = analogRead(soilPin2); // read sig value from sensor 3
  digitalWrite(soilPower2, LOW); // turn D9 off
  return val2; // send current moisture value 
}
