import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_scenario.flip_kart_page import Flipkart_Page


class TestLogin:
    @pytest.fixture()

    def test_launch_url(self):
        print("sucessfully launch the flipkart site")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.flipkart.com")
        self.driver.maximize_window()
        self.driver.element_click()
        act_title = self.driver.title
        expected_title = "FLIPKART"
        if act_title == expected_title:
            assert True
            self.driver.implicitly_wait(3)

    def test_login(self):
        print("Successfully launched the Flipkart site")
        # self.driver = webdriver.Chrome()
        self.page = Flipkart_Page(self.driver)
        self.page.element_click()
        time.sleep(2)


    # def test_search(self):
    #     print("sucessfully launch the flipkart site")
    #     self.driver = webdriver.Chrome()
    #     self.page = Flipkart_Page(self.driver)
    #     self.page.element_search(self.search)
    #     act_dashboard_text = self.driver.find_element(By.XPATH, "//*[@id='container']").text
    #     if act_dashboard_text == "dashboard":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.close()
    #         assert False
    # def test_pen_drive(self):
    #     print("sucessfully see the pendrive")
    #     self.driver = webdriver.Chrome()
    #     self.page = Flipkart_Page(self.driver)
    #     self.page.element_click_pen_drive()
    #     self.driver.execute_script("window.scrollBy(0,500):")
    #     # print(driver.execute_script("return window.pageYOffset;"))
    #     time.sleep(6)
    #
    # def test_read_more(self):
    #     self.driver = webdriver.Chrome()
    #     self.page = Flipkart_Page(self.driver)
    #     self.page.element_click_read_more()
    #     time.sleep(6)
