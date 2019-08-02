void webPageStandardMode(){
  Serial.print("Starting Web Server at ");
  Serial.println(WiFi.localIP());
  delay(8000);

  webPage += "<h1 align=\"center\" style=\"color:green; front-size:3em\">Connect to router</h1>";
  webPage += "<table width=\"100%\" height=\"90%\" border=\"3\" bordercolor=\"Gray\" background=\"blue\" cellpadding=\"4\">";
  webPage += "<tr  align=\"right\" border=\"1\" valign=\"top\">";
  webPage += "<td height=\"10%\" width=\"75%\"><div align=\"center\"><h2 style=\"color: red; font-size: 2em\">Comand button</h2>";
  webPage += "<a href=\"Calibrate\"><button>Calibrate</button></a><a style=\" margin-left: 20px\" href=\"GetParam\"><button>Get dimensions</button></a></div></td>";
  webPage += "<td><div align=\"center\"><p>Check ESP</p><a href=\"socket2On\"><button>LED OFF</button></a>";
  webPage += "<a href=\"socket2Off\"><button>LED ON</button></a></div></td></tr>";
  webPage += "<tr align=\"right\" border=\"1\" valign=\"top\"><td><div align=\"center\" style=\"margin-top: 10px\">";
  webPage += "<form metod=\"get\" action=\"codePlusGet\"><input autofocus name=\"code\" length=64 type=\"number\"></form>";
  webPage += "<table width=\"700px\" height=\"500px\" border=\"2\" bordercolor=\"black\" style=\"background-color: ";
  webPage += "LightGrey; margin-top: 20px\" cellpadding=\"8\"><tr></tr>";
  
  webPageEnd = "</table></div></td><td><p> Reset Log<a href=\"reset\"><button>RESET</button></a></p><p><a href=\"/resetPass\">Reset Wi-Fi Settings</a></p></td></tr></table>";
 

  webServer.on("/", [](){
    webServer.send(200, "text/html",  makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
  });
  
  webServer.on("/Calibrate", [](){
     Serial.println("-c");
     webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
     delay(1000);
  });

  webServer.on("/GetParam", [](){
     Serial.println("-g");
     webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
     delay(1000);
  });

  webServer.on("/codePlusGet", [](){
    Serial.println(webServer.arg("code"));
    String code = urlDecode(webServer.arg("code"));
    Serial.print("Code: ");
    Serial.println(code);
    webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
    delay(1000);
  });

  webServer.on("/socket2Off", [](){
     Serial.println("IN socket2Off");
     Serial.println("socket Off");
     webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
     digitalWrite(gpio2_pin, LOW);
     delay(1000);
  });

  webServer.on("/socket2On", [](){
     Serial.println("socket On");
     webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
     digitalWrite(gpio2_pin, HIGH);
      delay(1000);
   });
// webServer.on("/sendParam", [](){
  
//           getAllParam();
          
//           webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
//           delay(1000);
//   });
  webServer.on("/reset", [](){
    tempMassage="";
    webServer.send(200, "text/html", makePage("HIT SYSTEM", webPage+tempMassage+webPageEnd));
    delay(100);
  });

  webServer.on("/resetPass", []() {
    resetEeprom();
    String s = "<h1>Wi-Fi settings was reset.</h1><p>Please reset device.</p>";
    webServer.send(200, "text/html", makePage("Reset Wi-Fi Settings", s));
  });
}



// void getAllParam(){
  
//     frontTemp=firebaseGetParam("Front");
//     sensTemp=firebaseGetParam("PARAM");
//     holdTemp=firebaseGetParam("HOLD");

//     if(frontTemp!=front||sensTemp!=sens||holdTemp!=hold){
//        if(holdTemp>50&&holdTemp<1000&&sensTemp>50&&sensTemp<1000&&frontTemp>50&&frontTemp<1000){
//            front=frontTemp;
//            sens=sensTemp;
//            hold=holdTemp;
    
//            sprintf(uartOut,"!?%03d:%03d:%03d\r\n",sens,front,hold);
//            Serial.println(uartOut);
//        }
//     }
// } 
