import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configuracion del navegador
chrome_options = Options()
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Acceder a la pagina
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
time.sleep(3)

# Enviar datos de Reset  (ERROR NO TIENE LINK - esos son ejemplos)
reset_password = driver.find_element(By.CLASS_NAME, "oxd-input")
reset_password.send_keys("admin")
reset_button = driver.find_element(By.CLASS_NAME, "oxd-button")
reset_button.click()

time.sleep(3)

# Salir
driver.quit()
