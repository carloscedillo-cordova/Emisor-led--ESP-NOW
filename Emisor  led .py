import network  # Importamos la librería de red para manejar Wi-Fi y ESP-NOW
import espnow  # Importamos la librería ESP-NOW para la comunicación directa entre ESP32
import machine  # Importamos la librería para manejar los pines GPIO del ESP32
import time  # Importamos la librería para manejar el tiempo de espera

# Inicializa la interfaz WLAN en modo estación (STA_IF)
sta = network.WLAN(network.STA_IF)
sta.active(True)  # Activamos la interfaz Wi-Fi
sta.disconnect()  # Nos desconectamos de cualquier red Wi-Fi previamente conectada

# Inicializa la comunicación ESP-NOW
esp = espnow.ESPNow()
esp.active(True)  # Activamos la comunicación ESP-NOW

# Configuración del pin del botón (puedes usar GPIO 0, 12, 13, etc.)
button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)  # Botón con resistencia pull-up

# Dirección MAC del receptor (reemplaza con la dirección MAC del receptor)
mac_receptor = b'\x24\x6F\x28\x58\x32\x74'  # Aquí va la dirección MAC del receptor

# Función para enviar un mensaje a través de ESP-NOW
def enviar_mensaje(mensaje):
    print(f"Enviando mensaje: {mensaje}")
    esp.send(mac_receptor, mensaje)  # Enviar el mensaje al receptor

# Bucle principal
while True:
    if button_pin.value() == 0:  # Si el botón está presionado (nivel bajo)
        print("Botón presionado, enviando mensaje 'ledOn'...")
        enviar_mensaje(b'ledOn')  # Enviar mensaje para encender el LED
        time.sleep(0.5)  # Esperar para evitar rebotes del botón (debouncing)

    else:
        print("Botón no presionado, enviando mensaje 'ledOff'...")
        enviar_mensaje(b'ledOff')  # Enviar mensaje para apagar el LED
        time.sleep(0.5)  # Esperar para evitar rebotes del botón (debouncing)
