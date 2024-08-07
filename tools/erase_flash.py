import subprocess
from ports import detect_ports
from chip_id import detect_chip

def erase_flash():
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
    erase_flash_cmd = f"esptool --chip {chip_type} --port {port} erase_flash"

    subprocess.run(erase_flash_cmd, shell=True, check=True)
    print("Flash borrado exitosamente.")

if __name__ == "__main__":
    erase_flash()
