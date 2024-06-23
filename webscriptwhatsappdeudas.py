import requests
import pywhatkit
import time
from datetime import datetime, timedelta

# URL del servicio
url = "http://127.0.0.1:8000/deudas"

# Formatear Fechas
def formatear_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%a, %d %b %Y')
        return fecha.strftime('%d/%m/%Y')
    except ValueError:
        try:
            fecha = datetime.strptime(fecha_str, '%a, %d %b %Y %H:%M:%S %Z')
            return fecha.strftime('%d/%m/%Y')
        except ValueError:
            return fecha_str  # Si no se puede parsear, devuelve la cadena original

# Realizar la solicitud HTTP para obtener los datos
response = requests.get(url)
deudas = response.json()

# Obtener la fecha actual en el formato adecuado
fecha_actual = datetime.now().strftime("%a, %d %b %Y")

# Obtener la hora actual y añadir un minuto
tiempo_envio = datetime.now() + timedelta(minutes=1)
hora_envio = tiempo_envio.hour
minuto_envio = tiempo_envio.minute
cerrar = 3

#Saludos
def obtener_saludo():
    hora_actual = datetime.now().hour
    if 5 <= hora_actual < 12:
        return "Buenos días"
    elif 12 <= hora_actual < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"

def generar_mensaje(nombre, descripcion, valor_adeudado, fecha_pago, fecha_max, saldo):
    saludo = obtener_saludo()
    
    mensaje = f"""¡{saludo}, estimado/a {nombre}! 👋

🔔 Recordatorio amistoso sobre su pago pendiente:

📝 {descripcion}
💰 Valor a cancelar: ${valor_adeudado}
📅 Fecha de corte: {formatear_fecha(fecha_pago)}
📅 Fecha máxima de pago: {formatear_fecha(fecha_max)}
💼 Saldo actual: ${saldo}

🌟 ¡Mantenga al día sus pagos y disfrute de nuestros servicios sin interrupciones!

💡 Consejo: Pagar a tiempo le ayuda a mantener un buen historial crediticio.

¿Necesita ayuda? Estamos aquí para asistirle. No dude en contactarnos si tiene alguna pregunta.

¡Que tenga un excelente dia! 😊
"""
    return mensaje


# Iterar sobre las deudas y enviar los mensajes si la fecha coincide
for deuda in deudas:
    numero = deuda['phone']
    descripcion = deuda['descripcion']
    valor_adeudado = deuda['valor_adeudado']
    saldo = deuda['saldo']
    nombre = deuda['name']
    fecha_pago_completa = deuda['fecha_pago']
    fecha_maxima=deuda['fecha_maxima']
    fecha_pago = " ".join(fecha_pago_completa.split()[:4])

    # Comprobar si la fecha de pago es igual a la fecha actual
    if fecha_pago == fecha_actual:
        # Obtener solo la hora y el minuto de la fecha_pago
        hora_minuto_pago = fecha_pago_completa.split(" ")[4][:5]
        
        mensaje = generar_mensaje(nombre, descripcion, valor_adeudado, fecha_pago,fecha_maxima, saldo)
        print(mensaje)

        # Enviar el mensaje
        pywhatkit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio, 10, cerrar, cerrar)
        print(f"Mensaje programado para {numero} a las {hora_envio}:{minuto_envio}")
        
        # Aumentar el minuto para el siguiente mensaje
        minuto_envio += 1

        # Ajustar la hora y minutos si se pasa de 59
        if minuto_envio >= 60:
            minuto_envio = 0
            hora_envio += 1
        
        # Esperar un poco antes de programar el siguiente mensaje para evitar problemas
        time.sleep(20)  # Espera 20 segundos para evitar conflictos (puedes ajustar este tiempo)

print("Todos los mensajes han sido programados.")
