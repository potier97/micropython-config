import subprocess
import sys
from ports import detect_ports
from chip_id import detect_chip


def flash_esp32(erase=False):
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

    write_flash_cmd = ""
    if chip_type == "esp32":
        print("Flasheando ESP32...")
        write_flash_cmd = f"esptool --chip {chip_type} --port {port} --baud 460800 write_flash -z 0x1000 ./firmware(ESP32_GENERIC-20240602-v1.23.0.bin"
    elif chip_type == "esp8266":
        print("Flasheando ESP8266...")
        write_flash_cmd = f"esptool --chip {chip_type} --port {port} --baud 460800 write_flash --flash_freq 40m --flash_mode dio --flash_size detect 0  ./firmware/ESP8266_GENERIC-20180511-v1.9.4.bin"
    else:
        print("Tipo de chip no soportado.")
        return

    if erase:
        erase_flash_cmd = f"esptool --chip {chip_type} --port {port} erase_flash"
        subprocess.run(erase_flash_cmd, shell=True, check=True)
        print("Flash borrado exitosamente.")

    print(f"Comando de flasheo: {write_flash_cmd}")
    subprocess.run(write_flash_cmd, shell=True, check=True)
    print("Flasheo completado.")


if __name__ == "__main__":
    #if len(sys.argv) < 2:
    #    print("Uso: python flash.py <ruta_al_firmware> [--erase]")
    #    sys.exit(1)
    #firmware_path = sys.argv[1]
    
    erase = '--erase' in sys.argv
    flash_esp32(erase)