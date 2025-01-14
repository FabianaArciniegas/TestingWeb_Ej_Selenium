import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ImplicitWaits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        service = Service("../drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(options=chrome_options, service=service)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.implicitly_wait(time_to_wait=3)

    def test_login_page(self):
        title_login_page = self.driver.title
        self.assertEqual(title_login_page, "OrangeHRM")

    def test_validate_login(self):
        username = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password.send_keys("admin123")
        button_login = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button_login.click()
        time.sleep(3)

        menu = self.driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']")
        self.assertTrue(menu.is_displayed(), msg="El login no se realiza de manera satisfactoria")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
