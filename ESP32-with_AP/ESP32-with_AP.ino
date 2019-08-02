/*
 *
 * VHH_ESP
 *
*/

//#include "FirebaseESP8266.h" //FirebaseESP8266.h must be included before ESP8266WiFi.h
#include <ESP8266WiFi.h>

#include <EEPROM.h>
#include <DNSServer.h>                  // ??? realy need?
#include <WiFiClient.h>                 // ??? realy need?
#include <ESP8266WebServer.h>

#include <ArduinoJson.h>

//#define FIREBASE_HOST "testflayhit.firebaseio.com" //Do not include https:// in FIREBASE_HOST
//#define FIREBASE_AUTH "ZMoj3OzKbys4MXaz7K95gd58nOMsgF0x9KHsfnoG"

//-------------====___SET your ID device__=====------------------
          String path = "/HS1";
//---------------------------------------------------------------

String jsonStr;
char uartOut[20];
int sens=250,hold=350,front=50,
    sensTemp=0,holdTemp=0, frontTemp=0;

    String incomingByte ="";
    String message ="";
    String simbol = "";

    StaticJsonDocument<200> doc; //for Json

// AP acscess point param
const IPAddress apIP(192, 168, 1, 1);
const char* apSSID = "ESP8266_SETUP";
boolean settingMode;
String ssidList;


//Define FirebaseESP8266 data object
//FirebaseData firebaseData;
//Local server
DNSServer dnsServer;                     // ??? realy need?
ESP8266WebServer webServer(80);

    String webPage = "";
    String webPageEnd = "";
    String tempMassage="";
    int count =1; 

  int gpio2_pin = 2;
//---------------------------------------------------------------------------------------------------------------
//===================================================__SETUP__===================================================
//---------------------------------------------------------------------------------------------------------------
void setup()
{

  Serial.begin(115200);
  EEPROM.begin(512);
  delay(100);

  // подготавливаем GPIO-контакты:
  pinMode(gpio2_pin, OUTPUT);
  digitalWrite(gpio2_pin, LOW);
 
     incomingByte+="Measurment "+String(count)+" : ";

  if (restoreConfig()) {             // check SSID and pass in EEPROM
    if (checkConnection()) {         // ckeck  WI-FI connect
      settingMode = false;
      startWebServer();              // run normal page
     
      //Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
      //Firebase.reconnectWiFi(true);

          delay(4000);
          Serial.println("----------Begin Set Test-----------");
          Serial.println();
          //Serial.println("hi\r\n");
          Serial.print("-i");
          Serial.println(WiFi.localIP());

        //  firebasePushIp();
          //delay(2000);
         // getAllParam();
      return;
    }
  }
  settingMode = true;
  setupMode();                       // run page set SSID and pass

}

void loop()
{
  
  if (settingMode) { 
      dnsServer.processNextRequest(); 
      }
  webServer.handleClient();
  
  if (Serial.available() > 0) { //если есть доступные данные
        // считываем байт
    simbol = String(Serial.read() - 48);
  
    if ( checkChar() ) {
          
          Serial.println(message);
          DeserializationError error = deserializeJson(doc, message);

          // Test if parsing succeeds.
          if (error) {
            Serial.print(F("deserializeJson() failed: "));
            Serial.println(error.c_str());
            //return;
          }
          else{
            int Weight = doc["Weight"];//"Width\": %4d,\"Height\": %4d
            int Length = doc["Length"];
            int Width = doc["Width"];
            int Height = doc["Height"];
            tempMassage += "<tr height=\"10px\" ><td ><p>"+incomingByte+"</p></td>"; 
            tempMassage += "<td><p>Weight: " + String(Weight) + "gram</p></td>";
            tempMassage += "<td><p>Length: " + String(Length) + "cm</p></td>";
            tempMassage += "<td><p>Width: " + String(Width) + "cm</p></td>";
            tempMassage += "<td><p>Height: " + String(Height) + "cm</p></td></tr>";
            count++;
          }      

    
      if(message=="re"){
           resetEeprom();
      }
      else {

          //firebasePush();

         // getAllParam();
          
          simbol = "";
          // count++;
          incomingByte = "";
          message="";
          Serial.println("reset message");
          incomingByte += "Measurment " + String(count) + " : ";
        }
     }
     else {
          message += simbol;
        }
  }
}


void startWebServer() {
  if (settingMode) {
    webPageSetupMode();}
  else {
    webPageStandardMode();
  }  
  webServer.begin();
  
}
