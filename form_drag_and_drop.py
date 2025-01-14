import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configuracion del navegador
chrome_options = Options()
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Acceder a la página
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(3)

# Drag and Drop (ok)
action_chains = ActionChains(driver)

# Buscar los elementos y darle movimiento
source_element_1 = driver.find_element(By.ID, "box7")
target_element_1 = driver.find_element(By.ID, "box107")
action_chains.drag_and_drop(source=source_element_1, target=target_element_1).perform()
time.sleep(3)

source_element_2 = driver.find_element(By.ID, "box5")
target_element_2 = driver.find_element(By.ID, "box105")
action_chains.drag_and_drop(source=source_element_2, target=target_element_2).perform()
time.sleep(3)

# Salir
driver.quit()
