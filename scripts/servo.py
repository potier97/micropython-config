import machine
import time
from servo import Servo

led = machine.Pin(16, machine.Pin.OUT)
# Configura el pin PWM
#servo_pin = machine.Pin(14, machine.Pin.OUT)  # Cambia el pin si es necesario
#pwm = machine.PWM(servo_pin, freq=50)
motor=Servo(pin=14)
# Función para establecer el ángulo del servo
#def set_servo_angle(angle):
#    # Convierte el ángulo (0-180) a un ciclo de trabajo de PWM
#    duty = int((angle / 180.0 * 102) + 26)
#    pwm.duty(duty)

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