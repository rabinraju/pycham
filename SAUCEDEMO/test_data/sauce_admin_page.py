import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Login_Page:
    text_username_id = "user-name"
    text_password_id ="password"
    button_login_xpath = "//*[@id='login-button']"
    cart_xpath = "//*[@id='shopping_cart_container']/a"
    add_to_cart_xpath = "//*[@id='add-to-cart-sauce-labs-backpack']"
    click_filter_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[2]"
    checkout_xpath = "//*[@id='checkout']"
    checkout_firstname_id = "input[data-test='firstName']"
    checkout_lastname_id = "input[data-test='lastName']"
    checkout_postalcode_id = "postal-code"
    checkout_continue_xpath = "//*[@id='continue']"


    def __init__(self,driver):
        self.driver = driver

    def element_username(self,username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID,self.text_username_id).send_keys(username)

    def element_password(self,password):
        self.driver.find_element(By.ID,self.text_password_id).clear()
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_cart_button(self):
        self.driver.find_element(By.XPATH,self.cart_xpath).click()

    def click_filter_button(self):
        self.driver.find_element(By.XPATH,self.click_filter_xpath).click()

    def click_checkout_button(self):
        self.driver.find_element(By.XPATH,self.checkout_xpath).click()

    def click_checkout_first_name(self,FirstName):
        self.driver.find_element(By.XPATH,self.checkout_firstname_id).clear()
        self.driver.find_element(By.XPATH,self.checkout_firstname_id).send_keys(FirstName)

    def click_checkout_last_name(self,LastName):
        self.driver.find_element(By.XPATH,self.checkout_lastname_id).clear()
        self.driver.find_element(By.XPATH,self.checkout_lastname_id).send_keys(LastName)

    def click_checkout_postal_code(self,postal_code):
        self.driver.find_element(By.ID,self.checkout_postalcode_id).clear()
        self.driver.find_element(By.ID,self.checkout_postalcode_id).send_keys(postal_code)

    def click_checkout_continue_xpath(self):
        self.driver.find_element(By.XPATH,self.checkout_continue_xpath).click()

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH,self.add_to_cart_xpath).click()
        self.driver.

