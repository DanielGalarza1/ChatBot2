import pywhatkit
import time

# Lista de números de teléfono
numeros = ["+593987860206", "+593995583574", "+593987974242"]


# Mensaje a enviar
mensaje = "Hola esto es una prueba"

# Hora y minuto inicial en que se enviará el primer mensaje
hora_envio = 20
minuto_envio = 49
cerrar= 3
si = True


# Ciclo para enviar el mensaje a cada número
for numero in numeros:
    pywhatkit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio, 10, cerrar, cerrar)
    print(f"Mensaje programado para {numero} a las {hora_envio}:{minuto_envio}")
    
    # Aumentar el minuto para el siguiente mensaje
    minuto_envio += 1

    # Ajustar la hora y minutos si se pasa de 59
    if minuto_envio >= 60:
        minuto_envio = 0
        hora_envio += 1
    
    # Esperar un poco antes de programar el siguiente mensaje para evitar problemas
    time.sleep(20)  # Espera 10 segundos para evitar conflictos (puedes ajustar este tiempo)

print("Todos los mensajes han sido programados.")