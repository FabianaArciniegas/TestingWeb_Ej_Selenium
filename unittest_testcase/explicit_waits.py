import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ExplicitWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        service = Service("../drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(options=chrome_options, service=service)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_login_page(self):
        title_login_page = self.driver.title
        self.assertEqual(title_login_page, "OrangeHRM")

    def test_validate_login_and_logout(self):
        wait = WebDriverWait(self.driver, 10)

        username = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Username']")))
        username.send_keys("Admin")
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
        password.send_keys("admin123")
        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        button_login.click()

        logout = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")))
        logout.click()
        logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()

        title_page = self.driver.title
        wait.until(EC.title_contains("OrangeHRM"))
        self.assertEqual(title_page, "OrangeHRM")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
