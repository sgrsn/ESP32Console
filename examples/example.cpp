#include "print_server.hpp"

DumpServer debug;

void setup() {
  debug.print("Setup started");
  WiFi.softAP("MyESP32", "12345678");
  debug.begin();
  debug.print("Setup completed");
}

void loop() {
  debug.print(millis(), ": Looping...");
  delay(2000);
}