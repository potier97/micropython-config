import mfrc522
from machine import Pin, SPI
from time import sleep

# Inicializa el LED
led = Pin(16, Pin.OUT)

# # Configuración del lector RFID
sck = Pin(14, Pin.OUT)
mosi = Pin(13, Pin.OUT)
miso = Pin(12, Pin.IN)

print("Escanea una tarjeta RFID...")

# Función para leer la tarjeta y obtener el UID
def read_rfid():
    spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
    spi.init()
    rdr = mfrc522.MFRC522(spi, gpioRst=5, gpioCs=4)

    print("Escaneando tarjetas RFID...")

    while True:
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, uid) = rdr.anticoll()
            if stat == rdr.OK:
                print("Tarjeta detectada!")
                print("type: 0x%02x" % tag_type)
                print("UID: %02x%02x%02x%02x" % (uid[0], uid[1], uid[2], uid[3]))
                # Enciende el LED para indicar que se ha leído la tarjeta
                led.value(1)
                sleep(1)
                led.value(0)

# Ejecutar la lectura
read_rfid()
