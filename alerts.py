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

# Acceder a la página
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# Alerts - aceptar (ok)
button_alert = driver.find_element(By.ID, "confirmBtn")
button_alert.click()
time.sleep(3)

# Dar click en el boton aceptar
driver.switch_to.alert.accept()
time.sleep(3)

# Alerts - cancelar (ok)
button_alert = driver.find_element(By.ID, "confirmBtn")
button_alert.click()
time.sleep(3)

# Dar click en el boton cancelar
driver.switch_to.alert.dismiss()
time.sleep(3)

# Salir
driver.quit()
