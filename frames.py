from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configuracion del navegador
chrome_options = Options()
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()

# Acceder a la página
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# Frame (ejemplo)

# Para redirigirse al frame
driver.switch_to.frame("hola")

# Para cambiar el foto al marco-frame predeterminado
driver.switch_to.default_content()

# Para redirigirse al frame2
driver.switch_to.frame("hola2")

# Para cambiar el foto al marco-frame predeterminado
driver.switch_to.default_content()

# Salir
driver.quit()
