import pywhatkit
import time
import requests
import pyautogui
from datetime import datetime, timedelta

# Obtener números de teléfono del servicio web
response = requests.get('http://127.0.0.1:8000/usersphone')
if response.status_code == 200:
    data = response.json()  # Asumiendo que la respuesta es JSON
    numeros = [item['phone'] for item in data]
else:
    print("Error al obtener los números de teléfono.")
    numeros = []

# Obtener el mes actual en español
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes_actual = meses[datetime.now().month - 1]

# Mensaje a enviar
mensaje = f"""🎉 ¡OFERTAS EXPLOSIVAS DE {mes_actual.upper()}! 🎉

🔥 No te pierdas nuestros descuentos increíbles:
   ✅ Hasta 50% OFF en productos seleccionados
   ✅ 2x1 en accesorios
   ✅ Envío GRATIS en compras mayores a $50

⏰ ¡APÚRATE! Ofertas válidas solo por este mes.

👉 Visita nuestra tienda online: [URL de tu tienda]
o escríbenos para más información.

#Ofertas{mes_actual.capitalize()} #Descuentos #NoTeLoPierdas"""

# Ruta de la imagen a enviar
ruta_imagen = "C:/Users/Daniel/Desktop/Publicidades/Formateo.png"

# Obtener la hora actual y añadir un minuto
tiempo_envio = datetime.now() + timedelta(minutes=1)
hora_envio = tiempo_envio.hour
minuto_envio = tiempo_envio.minute
cerrar = 3

# Ciclo para enviar el mensaje y la imagen a cada número
for numero in numeros:
    pywhatkit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio, 15, cerrar, cerrar)
    print(f"Mensaje programado para {numero} a las {hora_envio}:{minuto_envio}")
   
    # Esperar un poco antes de enviar la imagen
    time.sleep(10)
   
    # Enviar imagen
    pywhatkit.sendwhats_image(numero, ruta_imagen)
    print(f"Imagen programada para enviar a {numero}")

    # Aumentar el minuto para el siguiente mensaje
    minuto_envio += 1  # Aumentamos 1 minutos para dar tiempo a que se envíe la imagen

    # Ajustar la hora y minutos si se pasa de 59
    if minuto_envio >= 60: 
        
        minuto_envio = minuto_envio % 60
        hora_envio += 1
   
    # Esperar un poco antes de programar el siguiente mensaje para evitar problemas
    time.sleep(10)  # Espera 5 segundos para evitar conflictos 
print("Todos los mensajes e imágenes han sido enviados.")
