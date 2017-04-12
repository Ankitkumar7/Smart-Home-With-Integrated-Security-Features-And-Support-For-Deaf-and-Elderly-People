#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile

RH_ASK driver;
const int ledPin = 11; 
void setup()
{
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600); // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}

void loop()
{
    uint8_t buf[17];
    uint8_t buflen = sizeof(buf);
    if (driver.recv(buf, &buflen)) // Non-blocking
    {
      int i;
      // Message with a good checksum received, dump it.
      Serial.print("Message: ");
      Serial.println((char*)buf);      
      digitalWrite(ledPin, HIGH);   
      delay(2000);
      digitalWrite(ledPin, LOW);
      delay(2000);
      
      
      
    }
    
    if (driver.recv(buf==0, &buflen==0)) // Non-blocking
    {
      int i;
      // Message with a good checksum received, dump it.
      Serial.print("Message: ");
      digitalWrite(ledPin, LOW);   
       
      Serial.println((char*)buf);      
        
      

    }
}
 


