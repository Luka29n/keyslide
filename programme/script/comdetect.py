import serial.tools.list_ports

def get_com_ports():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if "Arduino Leonardo" in desc:  
            print("{}: {}".format(port, desc))
            return port  
    print("Arduino Leonardo non trouvé.")  
    return None

port_com = get_com_ports()  

if port_com is not None:
    with open(r"C:\Users\lukap\Desktop\électronique\streamdeck\programme\script\deej-0.9.10\config.yaml", 'r') as file:
        lines = file.readlines()

    lines[19] = f"com_port: {port_com}\n"  

    with open(r"C:\Users\lukap\Desktop\électronique\streamdeck\programme\script\deej-0.9.10\config.yaml", 'w') as file:
        file.writelines(lines)
