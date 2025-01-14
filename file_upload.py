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

# File Upload (ok)
button_upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
time.sleep(5)
button_upload.send_keys(r"D:\Users\Dennys\Downloads\diagrama-clases-gein.drawio.png")
time.sleep(7)

# Salir
driver.quit()
