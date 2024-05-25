import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()
email = fake.email()
user_name = fake.user_name()
password = fake.password()
page_url_main = "http://127.0.0.1:8000/"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(page_url_main)
        self.driver.implicitly_wait(20)

    def testNoUserNameEntered(self):
        # 1. Click register btn
        sign_in_link = self.driver.find_element(By.CSS_SELECTOR,
                                                "a.btn.btn-outline-primary[href='/register/register/']")
        sign_in_link.click()

        # 2. Write e-mail
        email_input = self.driver.find_element(By.ID, "inputEmail")
        email_input.send_keys(email)

        # 2. Write password
        password_input = self.driver.find_element(By.ID, "inputPassword1")
        password_input.send_keys(password)

        # 2. Check password
        password2_input = self.driver.find_element(By.ID, "inputPassword2")
        password2_input.send_keys(password)

        # 3. Click btn
        register_account_btn = self.driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary")]')
        register_account_btn.click()

        # TEST
        get_url = self.driver.current_url
        if get_url == page_url_main:
            print("The test failed, managed to register without entering username")
        else:
            print("Test successful. Registration without a username failed.")

    def tearDown(self):
        self.driver.quit()


test = RegistrationTest()

