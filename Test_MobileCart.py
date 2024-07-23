import time

import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import *
from utilities.BaseClass import Base1
from utilities import *
from POM.HomePage import HomePage
import allure


@pytest.mark.usefixtures('get_sample12')
@pytest.mark.usefixtures('setup')
@allure.severity(allure.severity_level.NORMAL)
class Test_Mobile:
    def test_mobile(self, get_sample12):
        log = logg()
        self.driver.implicitly_wait(5)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        home = HomePage(self.driver)
        home.get_name().send_keys(get_sample12[0])
        home.get_email().send_keys(get_sample12[1])
        home.get_password().send_keys(get_sample12[2])
        home.get_checkbox().click()
        # self.driver.find_element(By.CSS_SELECTOR,"select#exampleFormControlSelect1")
        select = Select(home.get_select_box())
        select.select_by_visible_text(get_sample12[3])
        home.get_radio().click()
        home.get_success_button().click()

        cart = home.get_shoper_button()
        # cart = CartPage(self.driver)
        carts = cart.get_mobile_name()
        for cart1 in carts:
            log.debug(cart1.find_element(By.CSS_SELECTOR, "h4>a").text)
        a = self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']")
        log.debug(a.get_attribute('class'))
        mobile_carts = cart.get_cart()
        for mobile in mobile_carts:
            mobile.click()
        pre_check = cart.get_checkout()
        pre_check.get_cart_value()
        item_count = pre_check.get_item()
        for item in item_count:
            item.send_keys(Keys.BACKSPACE)
        for item in item_count:
            item.send_keys("2")

        final = pre_check.get_submit()
        final.get_country_val().send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul//a")))
        countries = final.get_suggestions()
        for country in countries:
            if country.text == 'India':
                country.click()
            break
        final.get_check_box().click()
        final.get_success_button().click()
        success_text = final.get_success_text()
        assert 'Success' in success_text
        allure.attach(self.driver.get_screenshot_as_png(),name='testingscreen',attachment_type=AttachmentType.PNG)

    @pytest.fixture(params=Base1.get_data1())
    def get_sample(self, request):
        return request.param

    @pytest.fixture()
    def get_sample12(self):
        return ['Vishnu','vish@12.com','vivdcd','Male']