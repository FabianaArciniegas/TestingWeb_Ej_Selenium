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
username = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
username.send_keys("Admin")
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("admin123")
time.sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
time.sleep(3)

# Formulario (ok)
menu_PIM = driver.find_element(By.LINK_TEXT, "PIM")
menu_PIM.click()
time.sleep(3)

PIM_config = driver.find_element(By.CSS_SELECTOR, "span[class='oxd-topbar-body-nav-tab-item']")
PIM_config.click()
time.sleep(1)
option_PIM_config = driver.find_element(By.LINK_TEXT, "Optional Fields")
option_PIM_config.click()
time.sleep(3)

# Analizar una opcion del checkbox
check1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
print("Seleccionado: " + str(check1.is_selected()))
print("Habilitado: " + str(check1.is_enabled()))
print("Visible en pantalla: " + str(check1.is_displayed()))

# Iterar sobre los checkbox
list_checkbox = driver.find_elements(By.XPATH,
                                     "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
button_save = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

for checkbox in list_checkbox:
    if checkbox.is_displayed() is True and checkbox.is_enabled() is False:
        button_save.click()
        time.sleep(2)
    if checkbox.is_displayed() is True and checkbox.is_selected() is False:
        checkbox.click()
        time.sleep(2)
    else:
        checkbox.click()

button_save.click()

# Salir
driver.quit()
