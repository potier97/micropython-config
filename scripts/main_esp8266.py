import machine
import time

led = machine.Pin(16, machine.Pin.OUT)
print("Hola, ESP8266!")

while True:
    led.value(not led.value())
    time.sleep(1)




