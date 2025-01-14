import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Configuracion del navegador
chrome_options = Options()
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Acceder a la página
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Login (ok)
username = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
username.send_keys("Admin")
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("admin123")
time.sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
time.sleep(3)

# Form (ok)
menu_admin = driver.find_element(By.LINK_TEXT, "Admin")
menu_admin.click()
time.sleep(3)

# Interacturar con las opciones
dropdown_user_role = driver.find_element(By.XPATH,
                                         "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]")
dropdown_user_role.click()
option_user_role = driver.find_element(By.XPATH, "//span[contains(text(),'ESS')]")
option_user_role.click()
time.sleep(3)

dropdown_status = driver.find_element(By.XPATH,
                                      "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]")
dropdown_status.click()
option_statis = driver.find_element(By.XPATH, "//span[contains(text(),'Enabled')]")
option_statis.click()
time.sleep(3)

# Dar click en el boton de buscar
button_search = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button_search.click()
time.sleep(3)

# Salir
driver.quit()

# Instancia Select
Select
