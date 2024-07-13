import subprocess
from ports import detect_ports

def upload_script(script_path, target_path):
    ports = detect_ports()
    if not ports:
        print("No se encontraron puertos disponibles.")
        return

    port = ports[0][0]  # Selecciona el primer puerto disponible
    print(f"Usando el puerto: {port}")

    upload_cmd = f"ampy --port {port} put {script_path} {target_path}"
    subprocess.run(upload_cmd, shell=True, check=True)
    print(f"Archivo {script_path} subido a {target_path} en el ESP32.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python upload_script.py <ruta_del_script_local> <ruta_del_script_en_esp32>")
        sys.exit(1)

    script_path = sys.argv[1]
    target_path = sys.argv[2]
    upload_script(script_path, target_path)
