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

# Table (solo ejemplo)
# Conocer la cantidad de filas y columnas
cols = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/td'))
rows = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr'))

# Iterar, para conocer los valores de la tabla
for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value)

# Cierre del navegador
driver.quit()
