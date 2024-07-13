import subprocess
from ports import detect_ports

def erase_flash():
    ports = detect_ports()
    if not ports:
        print("No se encontraron puertos disponibles.")
        return

    port = ports[0][0]  # Selecciona el primer puerto disponible
    print(f"Usando el puerto: {port}")

    erase_flash_cmd = f"esptool --chip esp32 --port {port} erase_flash"

    subprocess.run(erase_flash_cmd, shell=True, check=True)
    print("Flash borrado exitosamente.")

if __name__ == "__main__":
    erase_flash()
