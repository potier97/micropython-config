import subprocess
import sys
from ports import detect_ports


def flash_esp32(firmware_path, erase=False):
    ports = detect_ports()
    if not ports:
        print("No se encontraron puertos disponibles.")
        return

    port = ports[0][0]  # Selecciona el primer puerto disponible
    print(f"Usando el puerto: {port}")

    if erase:
        erase_flash_cmd = f"esptool --chip esp32 --port {port} erase_flash"
        subprocess.run(erase_flash_cmd, shell=True, check=True)
        print("Flash borrado exitosamente.")

    write_flash_cmd = f"esptool --chip esp32 --port {port} --baud 460800 write_flash -z 0x1000 {firmware_path}"
    subprocess.run(write_flash_cmd, shell=True, check=True)
    print("Flasheo completado.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python flash.py <ruta_al_firmware> [--erase]")
        sys.exit(1)

    firmware_path = sys.argv[1]
    erase = '--erase' in sys.argv
    flash_esp32(firmware_path, erase)