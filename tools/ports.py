import serial.tools.list_ports

def detect_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port, desc, hwid in sorted(ports):
        available_ports.append((port, desc))
    return available_ports

if __name__ == "__main__":
    ports = detect_ports()
    if ports:
        print("Puertos disponibles:")
        for port, desc in ports:
            print(f"{port}: {desc}")
    else:
        print("No se encontraron puertos disponibles.")
