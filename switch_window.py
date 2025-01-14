import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configuracion del navegador
chrome_options = Options()
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Acceder a la página
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Window (ok)
wait = WebDriverWait(driver, 10)
time.sleep(2)
link_main = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='OrangeHRM, Inc']")))
time.sleep(2)
link_main.click()
print(driver.current_window_handle)

# Retorna todos los valores de las ventanas abiertas del navegador
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "OrangeHRM":
        driver.close()

# Salir
driver.quit()
