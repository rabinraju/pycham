import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data.sauce_admin_page import Login_Page
from selenium.webdriver.common.keys import Keys

class TestAdminLogin:


    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    invalid_username = "SwagLabs"
    FirstName = "xydsfsdfz"
    LastName = "abcgsgds"
    postal_code = "12345"

    def test_sauce_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        current_title = self.driver.title
        expected_title = "Swag Labs"
        if current_title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\test_sauce_title.png")
            self.driver.close()
            assert False
    time.sleep(5)
    def test_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.login_page = Login_Page(self.driver)
        self.login_page.element_username(self.username)
        self.login_page.element_password(self.password)
        self.login_page.click_login_button()
        current_product_text = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
        if current_product_text == 'Product':
            assert True
            self.driver.back()
    time.sleep(10)

    def test_invalid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.login_page = Login_Page(self.driver)
        self.login_page.element_username(self.invalid_username)
        self.login_page.element_password(self.password)
        self.login_page.click_login_button()
        error_tologin = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text()
        if error_tologin == 'Epic sadface: Username and password do not match any user in this service':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
        #     self.driver.quit()

    def test_again_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.login_page = Login_Page(self.driver)
        self.login_page.element_username(self.username)
        self.login_page.element_password(self.password)
        self.login_page.click_login_button()
        time.sleep(13)
        current_product_text = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
        self.login_page.click_add_to_cart_button()
        time.sleep(5)
        self.login_page.click_filter_button()
        time.sleep(5)
        self.login_page.click_cart_button()
        time.sleep(5)
        self.login_page.click_checkout_button()
        time.sleep(13)
        if current_product_text == 'Product':
            assert True
            self.driver.implicitly_wait(4)
    time.sleep(10)

    def test_invalid_checkout(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.login_page = Login_Page(self.driver)
        self.login_page.click_checkout_first_name(self.FirstName)
        self.login_page.click_checkout_last_name(self.LastName)
        self.login_page.click_checkout_postal_code(self.postal_code)
        self.login_page.click_checkout_continue_xpath()

        try:
            # Use explicit wait to wait for the element to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span"))
            )
            current_CheckoutOverview = self.driver.find_element(By.XPATH,
                                                                "//*[@id='header_container']/div[2]/span").text

            if current_CheckoutOverview == 'Checkout: Overview':
                assert True
            else:
                assert False
        except NoSuchElementException:
            assert False
        finally:
            self.driver.close()

