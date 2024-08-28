from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import requests
import pytest


class Flipkart_Page:
    click_login = "//span[text()='Login']"


    def __init__(self, driver):
        self.driver = driver

    def element_click(self):
        self.driver.find_element(By.XPATH, self.click_login).click()

    # def element_click_read_more(self):
    #     self.driver.find_element(By.XPATH, self.click_read_more).click()
