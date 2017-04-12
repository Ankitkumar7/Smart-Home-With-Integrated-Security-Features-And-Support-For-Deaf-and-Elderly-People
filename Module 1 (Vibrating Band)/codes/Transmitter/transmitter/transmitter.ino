#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile

RH_ASK driver;
const int ledPin = 13;      // led connected to digital pin 13
const int knockSensor = 0; // the piezo is connected to analog pin 0
const int threshold = 100;  // threshold value to decide when the detected sound is a knock or not


int sensorReading = 0;      // variable to store the value read from the sensor pin
int ledState = LOW; 
void setup()
{
    Serial.begin(9600);   // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}

void loop()
{
   sensorReading = analogRead(knockSensor);
  if (sensorReading < threshold) {
    const char *msg = "Movement at the door, please check";
    driver.send((uint8_t *)msg, strlen(msg));
    driver.waitPacketSent();
    Serial.print("Done");
    delay(1000);
}
  


}
