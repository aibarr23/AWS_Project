
#include <SoftwareSerial.h>

// Attach the serial display's RX line to digital pin 2
SoftwareSerial mySerial(3,2); // pin 2 = TX, pin 3 = RX (unused)


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
int solenoidPin = 4;
int solenoidPin1 = 5;
int solenoidPin2 = 6;
int solenoidPin3 = 3;
int soilPin = A0;
int soilPin1 = A1;
int soilPin2 = A2;
int soilPower = 7;//Variable for Soil moisture Power
int soilPower1 = 8;
int soilPower2 = 9;  

void setup(){
  mySerial.begin(9600); // set up serial port for 9600 baud (speed)
  delay(500); // wait for display to boot up

  pinMode(soilPower, OUTPUT);//Set D7 as an OUTPUT
  digitalWrite(soilPower, LOW);//Set to LOW so no power is flowing through the sensor
}

void loop(){
  // Here we are declaring a string, which are lines of words,
  // and we want DisplayWords to be the words displayed on
  // the LCD screen, which will change based on whether the soil
  // wet or dry based on our threshold values above.
  String DisplayWords;

  // We need to set up a pin to get the value that the soil 
  // moisture sensor is outputting, so sensorValue will get the
  // analog value from the sensor pin A0 on the redboard that we 
  // set up earlier.

  int sensorValue;
  sensorValue = readSoil();

  // move cursor to beginning of first line on LCD:
  mySerial.write(254); 
  mySerial.write(128);

  // clear display:
  mySerial.write("                "); 
  mySerial.write("                ");

  // move cursor to beginning of first line of the LCD screen:
  mySerial.write(254); 
  mySerial.write(128);

  //Write what we want to desplay on the screen:
  mySerial.write("Water Level: ");
  mySerial.print(sensorValue); //Using .print instead of .write for values

  // Now we are going to check if the water level is below a 
  // out thresholdDown value we set earlier, and if it is have 
  // words "Dry, Water it!" display one column over on the first 
  // row:

  if (sensorValue <= thresholdDown){
    // move cursor to beginning of second line on LCD:
    mySerial.write(254); 
    mySerial.write(192);

    DisplayWords = "Dry, Water it!";
    mySerial.print(DisplayWords);

  // If the value is not below our thresholdDown value we want to 
  // check if it is above our thresholdUp value, and if it is 
  // change the display words to "Wet, Leave it!":



  } else if (sensorValue >= thresholdUp){
    // move cursor to beginning of second line on LCD:
    mySerial.write(254); 
    mySerial.write(192);

    DisplayWords = "Wet, Leave it!";
    mySerial.print(DisplayWords);

  // Otherwise if it is inbetween the two values we want it to 
  // the display it had, so if our soil was really wet and drying 
  // the words would only change to "Dry, Water it!" when it got to the lower threshold
  // (thresholdDown), but if it was dry and getting wetter the words
  // would only change to "Wet, Leave it!" when it got to the upper 
  // threshold (thresholdUp_):

  } else {
    // move cursor to beginning of second line on LCD:
    mySerial.write(254); 
    mySerial.write(192);

    mySerial.print(DisplayWords);
  }

  delay(500); //wait for half a second, so it is easier to read
}

//This is a function used to get the soil moisture content
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
int main() {
// function to open solenoids with weather prediction 
int perChance = 1;
// read in perChance
int sensorValue = readSoil();

 if (perChance < 30 && sensorValue < thresholdUp) {
  digitalWrite(solenoidPin, HIGH);
  delay(1000);
   delay(5*60*1000); //wait 5 minutes
   sensorValue = readSoil();
    if (sensorValue >= thresholdUp) {
      digitalWrite(solenoidPin, LOW);
      delay(1000);
    }
}
  else if (perChance <= 30 && sensorValue < thresholdUp) {
    delay(1*60*60*1000); //wait an hour
    sensorValue = readSoil();
        if (perChance < 30 && sensorValue < thresholdUp) {
          digitalWrite(solenoidPin, HIGH);
          delay(5*60*1000); //wait five minutes 
          sensorValue = readSoil(); 
          if (sensorValue >= thresholdUp) {
            digitalWrite(solenoidPin, LOW);
            delay(1000);

      
    } 
}
  }
  int sensorValue1 = readSoil1();
 if (perChance < 30 && sensorValue1 < thresholdUp) {
  digitalWrite(solenoidPin1, HIGH);
  delay(1000);
   delay(5*60*1000); //wait 5 minutes
   sensorValue1 = readSoil1();
    if (sensorValue1 >= thresholdUp) {
      digitalWrite(solenoidPin1, LOW);
      delay(1000);
    }
}
  else if (perChance <= 30 && sensorValue1 < thresholdUp) {
    delay(1*60*60*1000); //wait an hour
    sensorValue1 = readSoil1();
        if (perChance < 30 && sensorValue1 < thresholdUp) {
          digitalWrite(solenoidPin1, HIGH);
          delay(5*60*1000); //wait five minutes 
          sensorValue1 = readSoil(); 
          if (sensorValue1 >= thresholdUp) {
            digitalWrite(solenoidPin, LOW);
            delay(1000);

      
    } 
}
  }
 int sensorValue2 = readSoil2();
 if (perChance < 30 && sensorValue2 < thresholdUp) {
  digitalWrite(solenoidPin2, HIGH);
  delay(1000);
   delay(5*60*1000); //wait 5 minutes
   sensorValue2 = readSoil2();
    if (sensorValue2 >= thresholdUp) {
      digitalWrite(solenoidPin2, LOW);
      delay(1000);
    }
}
  else if (perChance <= 30 && sensorValue2 < thresholdUp) {
    delay(1*60*60*1000); //wait an hour
    sensorValue2 = readSoil2();
        if (perChance < 30 && sensorValue < thresholdUp) {
          digitalWrite(solenoidPin2, HIGH);
          delay(5*60*1000); //wait five minutes 
          sensorValue2 = readSoil2(); 
          if (sensorValue2 >= thresholdUp) {
            digitalWrite(solenoidPin2, LOW);
            delay(1000);

      
    } 
}
  }
}
