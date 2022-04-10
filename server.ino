
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

unsigned long previousMillis = 0;

boolean solenoidControl0 = false; // user is not controlling solenoid0
boolean solenoidControl1 = false; // user is not controlling solenoid1
boolean solenoidControl2 = false; // user is not controlling solenoid2
boolean solenoidControlOpen0 = false; // solenoid0 is not open
boolean solenoidControlOpen1 = false; // solenoid1 is not open
boolean solenoidControlOpen2 = false; // solenoid2 is not open
boolean returnControl = false; // microcontroller is currently in control of solenoids
boolean closeAll = false; // closing all solenoids is currently false

String Data;


/*

WiFi UDP Send and Receive String

This sketch wait an UDP packet on localPort using the WiFi module.

When a packet is received an Acknowledge packet is sent to the client on port remotePort

created 30 December 2012

by dlf (Metodo2 srl)

# Note following code was repurposed for a project use
*/

#include <SPI.h>
#include <WiFiNINA.h>
#include <WiFiUdp.h>
//#include "soil_moisture.h"

int status = WL_IDLE_STATUS;
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen on

char packetBuffer[256]; //buffer to hold incoming packet
char ReplyBuffer[] = "acknowledged"; // a string to send back

WiFiUDP Udp;

void setup() {
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

  //Initialize serial and wait for port to open:

  Serial.begin(9600);

  while (!Serial) {

    ; // wait for serial port to connect. Needed for native USB port only

  
  }

  // check for the WiFi module:

  if (WiFi.status() == WL_NO_MODULE) {

    Serial.println("Communication with WiFi module failed!");

    // don't continue
    while (true);

  }

  String fv = WiFi.firmwareVersion();

  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {

    Serial.println("Please upgrade the firmware");

  }

  // attempt to connect to Wifi network:

  while (status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);

  }

  Serial.println("Connected to wifi");
  printWifiStatus();
  Serial.println("\nStarting connection to server...");

  // if you get a connection, report back via serial:
  Udp.begin(localPort);
}

void loop() {
  int sensorValue;
  sensorValue = readSoil();

  int sensorValue1;
  sensorValue1 = readSoil1();

  int sensorValue2;
  sensorValue2 = readSoil2();
  
  if (returnControl == true) { //user returns control to solenoids
    solenoidControl0 = false; // user is not controlling solenoid0
    solenoidControl1 = false; // user is not controlling solenoid1
    solenoidControl2 = false; // user is not controlling solenoid2
  }
  
  

  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();

  if (packetSize > 0) {

    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remoteIp = Udp.remoteIP();
    Serial.print(remoteIp);
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    Udp.read(packetBuffer, 255);
    String Data(packetBuffer);
    Serial.println("Contents:");
    Serial.println(Data);

    //
    // check what the packet's purpose
    // packet format: [5 characters;content-->](content are dividie by ";")(5 characters represents its reason)
    // 5 Characters types:
    // WData: ; (this is for weather data) format-> Temperature;Feels like Temperature; Precipitation
    //


    // Get the data type the is inside of the packetBuffer
    int p = Data.indexOf(";");
    String DataT = Data.substring(0, 5); // this takes out the Data type in the packet buffer
    
    //this will send data to client
    if(DataT == "SData"){
      //collect data from controller
      // collect Solenoid status
      //digitalRead(solenoidPin);
      // collect moisture levels

      // test
      // send a reply, to the IP address and port that sent us the packet we received
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
      //ReplyBuffer = "store this data?";
      Udp.write(ReplyBuffer);
      Udp.endPacket();

    }

    // Update microcontroller of weather data.
    if(DataT == "WData") {

      //find first data value (Temperature)
      int p2 = Data.indexOf(";", p);
      p += 1;
      int s = p2 - p; // gives size of value
      String TempV = Data.substring(p, s);

      //find second data value(temp feeals like)
      p = p2;
      p2 = Data.indexOf(";",p);
      p += 1;
      s = p2 - p;
      String Tempfl = Data.substring(p, s);

      //find final data value(precipitation)
      p = p2;
      p2 = Data.length();
      p += 1;
      s = p2 - p;
      String Prec = Data.substring(p, s);

      //
      // now send extracted data to its needed location
      // so that the controller can make a decision
      //


      // send a reply, to the IP address and port that sent us the packet we received
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
      Udp.write(ReplyBuffer);
      Udp.endPacket();

    }
    memset(packetBuffer, 0, 255); // clear out packetBuffer array
  }


  unsigned long currentMillis = millis();
  if(sensorValue <= thresholdDown){//no timer
    if (solenoidControl0 == false) {
      
      wateringPot(sensorValue, solenoidPin);
      previousMillis = currentMillis;
    }
  }
  if(sensorValue >= thresholdDown){//wait for an hour
    if (solenoidControl1 == false) {
      if(currentMillis - previousMillis >= 3600000){
        
        wateringPot(sensorValue1, solenoidPin1);
        previousMillis = currentMillis;
      }
      
    }
  }
  if(sensorValue == thresholdDown){// wait 30 minutes
    if (solenoidControl2 == false) {
      if(currentMillis - previousMillis >= 1800000){
        
        wateringPot(sensorValue2, solenoidPin2);
        previousMillis = currentMillis;
      }
    }
  }


}

void printWifiStatus() {

  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");

}

int wateringPot (int sensorValue, int solenoidPin) { //what do i refer to high/low as?
  String x;
    if (solenoidPin == 11) {
    x = "S1";
  }
  else if (solenoidPin == 12){
    x = "S2";
  }
  else {
    x = "S3";
  }
  if (sensorValue <= thresholdDown) {
    //water it
    Data = x + "open";
    digitalWrite(solenoidPin, HIGH); //open solenoid
    delay(61000); //wait a minute and a second
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      delay(60000); //wait a minute
      Data = x + "close";
      digitalWrite(solenoidPin, LOW); //close solenoid
      delay(1000);
    }
    else {
      Data = x + "close";
      digitalWrite(solenoidPin, LOW); //close solenoid
      delay(1000);
    }
  }
  else if (sensorValue >= thresholdUp) {
    //wait and check later
    // delay(36000000); //wait an hour
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      Data = x + "open";
      digitalWrite(solenoidPin, HIGH); //open solenoid
      delay(61000); //wait a minute and a second
      sensorValue = readSoil();
      if (sensorValue <= thresholdDown) {
        delay(60000); //wait a minute
        Data = x + "close";
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
      else {
        Data = x + "close";
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
    }
  }
  else {
    // delay(18000000); //wait 30 min
    sensorValue = readSoil();
    if (sensorValue <= thresholdDown) {
      Data = x + "open";
      digitalWrite(solenoidPin, HIGH); //open solenoid
      delay(61000); //wait a minute and a second
      sensorValue = readSoil();
      if (sensorValue <= thresholdDown) {
        delay(60000); //wait a minute
        Data = x + "close";
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
      else {
        Data = x + "close";
        digitalWrite(solenoidPin, LOW); //close solenoid
        delay(1000);
      }
    }
  }
  packData(Data);
}

void solenoids(bool solenoidControl, bool solenoidControlopenclose, int So) {

  int solenoids[] = {0, 10, 11, 12};

  if (solenoids[So] == 0) { //closing all solenoids, microcontrller is still not in control
    digitalWrite(solenoidPin, HIGH);
    digitalWrite(solenoidPin1, HIGH);
    digitalWrite(solenoidPin2, HIGH);
  }
  else{
    if (solenoidControl == true) { //user interacts with solenoid0 switch
      if (solenoidControlopenclose == true) { //user opens solenoid
        digitalWrite(solenoids[So], HIGH);
      }
      else if (solenoidControl == false){ //close solenoid when it is open
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
    Data = "m1" +  String(val);
    packData(Data);
    return val;//send current moisture value
}

int readSoil1()
{
  digitalWrite(soilPower1, HIGH); // turn d8 on
  delay(10); //wait 10 milliseconds
  int val1 = analogRead(soilPin1); //Read the SIG value from sensor 2
  digitalWrite(soilPower1, LOW); // turn D8 off
  Data = "m2" +  String(val1);
  packData(Data);
  return val1; //send current moisture value
}
int readSoil2()
{
  digitalWrite(soilPower2, HIGH); // TURN D9 on
  delay(10); // wait 10 milliseconds
  int val2 = analogRead(soilPin2); // read sig value from sensor 3
  digitalWrite(soilPower2, LOW); // turn D9 off
  Data = "m3" +  String(val2);
  packData(Data);
  return val2; // send current moisture value
}


void packData (String water) {
  char packet[20];
  water = "update;" + water;
  water.toCharArray(packet, 20);
  Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
  Udp.write(packet);
  Udp.endPacket();
}
