import subprocess
from ports import detect_ports

def detect_chip(port):
    chip_info_cmd = f"esptool --port {port} chip_id"
    result = subprocess.run(chip_info_cmd, shell=True, capture_output=True, text=True)

    if "Chip is ESP8266" in result.stdout:
        return "esp8266"
    elif "Chip is ESP32" in result.stdout:
        return "esp32"
    else:
        return None

def read_mac():
    ports = detect_ports()
    if not ports:
        print("No se encontraron puertos disponibles.")
        return

    port = ports[0][0]  # Selecciona el primer puerto disponible
    print(f"Usando el puerto: {port}")

    chip_type = detect_chip(port)
    if not chip_type:
        print("No se pudo determinar el tipo de chip.")
        return

    print(f"Tipo de chip detectado: {chip_type}")

if __name__ == "__main__":
    read_mac()