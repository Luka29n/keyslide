import serial
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import math
from serial.tools import list_ports
import screen_brightness_control as sbc  # Bibliothèque pour ajuster la luminosité

# Fonction pour détecter automatiquement le port de l'Arduino
def find_arduino_port():
    ports = list_ports.comports()  # Liste les ports disponibles
    for port in ports:
        if 'Arduino' in port.description:  # Chercher un port avec "Arduino" dans la description
            print(f"Arduino détecté sur le port : {port.device}")
            return port.device
    raise Exception("Port Arduino non détecté")  # Si aucun Arduino n'est trouvé

# Détecter le port Arduino
arduino_port = find_arduino_port()

# Configuration du port série avec le port détecté
ser = serial.Serial(arduino_port, 9600)
time.sleep(2)  # Attendre que la connexion soit établie

# Fonction pour initialiser le contrôle du volume
def get_audio_device():
    devices = AudioUtilities.GetSpeakers()  # Récupérer les haut-parleurs actifs
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

# Fonction pour ajuster le volume avec un mappage logarithmique
def set_volume(volume, percentage):
    volume_range = volume.GetVolumeRange()
    min_volume = volume_range[0]  # Volume minimum (généralement -65 dB)
    max_volume = volume_range[1]  # Volume maximum (généralement 0 dB)

    if percentage == 0:
        volume.SetMute(1, None)
        print(f"Potentiomètre à 0% : Son coupé")
    else:
        volume.SetMute(0, None)

        if percentage >= 98:  # Si le pourcentage est 98, 99 ou 100
            volume_level = max_volume
            print(f"Pourcentage : {percentage}%, Volume réglé à 100%")
        else:
            # Mappage logarithmique pour correspondre à la perception du son
            volume_level = min_volume + (1 - math.exp(-percentage / 25)) * (max_volume - min_volume)
            print(f"Réglage du volume à : {volume_level:.2f} dB")

        volume.SetMasterVolumeLevel(volume_level, None)

# Fonction pour ajuster la luminosité
def set_brightness(percentage):
    # Limiter le pourcentage entre 0 et 100
    percentage = max(0, min(percentage, 100))
    try:
        sbc.set_brightness(percentage)  # Ajuster la luminosité
        print(f"Luminosité réglée à : {percentage}%")
    except Exception as e:
        print(f"Erreur lors de la modification de la luminosité : {e}")

# Initialiser le contrôle du volume
volume = get_audio_device()

# Variable pour surveiller les changements de périphérique
last_device_id = None

while True:
    if ser.in_waiting > 0:
        try:
            # Lire la dernière ligne reçue
            data = ser.readline().decode('utf-8').strip()  # Lire la ligne et la convertir en chaîne

            # Vérifier que la donnée commence par 'a' ou 'b'
            if data[0] == 'a':
                # Extraire le pourcentage après le 'a'
                percentage = int(data[1:])  # Prendre tout après le 'a' et convertir en entier
                print(f"Potentiomètre (volume) : {percentage}%")

                # Vérifier si le périphérique a changé
                devices = AudioUtilities.GetSpeakers()
                current_device_id = devices.GetId()  # Obtenir l'ID du périphérique actif

                if current_device_id != last_device_id:
                    print("Changement de périphérique détecté. Réinitialisation du contrôle du volume.")
                    volume = get_audio_device()  # Réinitialiser l'interface de contrôle du volume
                    last_device_id = current_device_id

                set_volume(volume, percentage)  # Ajuster le volume

            elif data[0] == 'b':
                # Extraire le pourcentage après le 'b'
                percentage = int(data[1:])  # Prendre tout après le 'b' et convertir en entier
                print(f"Potentiomètre (luminosité) : {percentage}%")
                set_brightness(percentage)  # Ajuster la luminosité

            else:
                print(f"Lettre non reconnue : {data[0]}")
        except ValueError:
            print("Erreur de lecture des données")
    time.sleep(0.01)  # Délai réduit pour une meilleure réactivité
