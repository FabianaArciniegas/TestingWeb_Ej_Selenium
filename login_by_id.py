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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Login (ERROR NO TIENE ID LOS INPUTS - esos son ejemplos)
username = driver.find_element(By.ID, "txtUsername")
username.send_keys("Admin")
password = driver.find_element(By.ID, "txtPassword")
password.send_keys("admin123")
button = driver.find_element(By.ID, "btnLogin")
button.click()

time.sleep(3)

# Salir
driver.quit()
