#include <Arduino.h>
#include <PrintServer.h>

DumpServer debug;

void setup() {
  debug.print("Setup started");
  WiFi.softAP("DumpServer", "12345678");
  debug.begin();
  debug.print("Setup completed");
}

void loop() {
  debug.print(millis(), ": Looping...");
  delay(2000);
}