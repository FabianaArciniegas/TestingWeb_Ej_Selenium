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

# Login (ok)
username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
time.sleep(3)
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("admin123")
time.sleep(3)
button = driver.find_element(By.XPATH, "//button[@type='submit']")
button.click()

time.sleep(3)

# Salir
driver.quit()
