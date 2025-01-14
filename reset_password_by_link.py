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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Reset password (ERROR NO TIENE LINK - esos son ejemplos)
reset_password = driver.find_element(By.LINK_TEXT, "Forgot your password?")
reset_password2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot")
reset_password.click()

# Salir
driver.quit()
