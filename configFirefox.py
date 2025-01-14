import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Configuracion inicial del navegador
firefox_options = Options()
service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(options=firefox_options, service=service)
driver.maximize_window()

# Acceder a la página
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Esperar 3 segundos
time.sleep(3)

# Cerrar el navegador
driver.quit()
