import machine
import time
from servo import Servo

led = machine.Pin(16, machine.Pin.OUT)
motor=Servo(pin=14)

while True:
    # Mover el servo a 0 grados
    led.value(not led.value())
    motor.move(0) # tourne le servo à 0°
    time.sleep(0.5)
    led.value(not led.value())
    motor.move(90) # tourne le servo à 90°
    time.sleep(0.5)
    led.value(not led.value())
    motor.move(180) # tourne le servo à 180°
    time.sleep(0.5)
    led.value(not led.value())
    motor.move(90) # tourne le servo à 90°
    time.sleep(0.5)
    led.value(not led.value())
    motor.move(0) # tourne le servo à 0°
    time.sleep(0.5)