from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

# Inicializar el driver de Firefox
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

all_names = ['Alejo Munir Un']
msg = 'Esto es una prueba de web scraping'
count = 3

input('Presiona cualquier tecla después de escanear el código QR')

# Esperar a que la página cargue completamente
wait = WebDriverWait(driver, 10)

for name in all_names:
    try:
        # Esperar a que el contacto esté disponible y hacer clic
        user = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]')))
        user.click()

        # Esperar a que la caja de mensaje esté disponible
        msg_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
        
        for _ in range(count):
            msg_box.send_keys(msg)
            msg_box.send_keys(Keys.ENTER)  # Presionar Enter para enviar el mensaje
    except (NoSuchElementException, TimeoutException) as e:
        print(f'No se pudo enviar el mensaje a {name}: {e}')
    except Exception as e:
        print(f'Un error inesperado ocurrió con {name}: {e}')
