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

int status = WL_IDLE_STATUS;
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen on

char packetBuffer[256]; //buffer to hold incoming packet
char  ReplyBuffer[] = "acknowledged";       // a string to send back

WiFiUDP Udp;

void setup() {

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
    // check what the packet's purpose
    // packet format: [5 characters;content-->](content are dividie by ";")(5 characters represents its reason)
    // 5 Characters types:
    // WData: ; (this is for weather data) format-> Temperature;Feels like Temperature; Precipitation
    
    // Get the data type the is inside of the packetBuffer
    int p = Data.find_first_of(";");
    DataT = Data.substr(0, 5) // this takes out the Data type in the packet buffer
    // Update microcontroller of weather data.
    if(DataT == "WData") {
      //find first data value (Temperature)
      int p2 = Data.find_first_of(";", p);
      p += 1;
      int s = p2 - p; // gives size of value
      TempV = Data.substr(p, s);

      //find second data value(temp feeals like)
      p = p2;
      p2 = Data.find_first_of(";",p);
      p += 1;
      s = p2 - p;
      Tempfl = Data.substr(p, s);

      //find final data value(precipitation)
      p = p2;
      p2 = Data.length();
      p += 1;
      s = p2 - p;
      Prec = Data.substr(p, s);

      //
      // now send extracted data to its needed location
      // so that the controller can make a decision
      //


      // send a reply, to the IP address and port that sent us the packet we received
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());

      ReplyBuffer[] = "Weather Data Recieved"

      Udp.write(ReplyBuffer);

      Udp.endPacket();
      }
    memset(packetBuffer, 0, 255); // clear out packetBuffer array

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