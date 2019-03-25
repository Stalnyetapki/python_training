# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/projects/drivers/geckodriver/geckodriver.exe')
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://addressbook:81/group.php")

    def login(self, driver, username, password):
        # login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            ".//*[@id='LoginForm']/input[3]").click()

    def open_groups_page(self, driver):
        driver.find_element_by_name("new").click()

    def create_group(self, driver, name, header, footer):
        # init group creation
        driver.find_element_by_name("group_name").click()
        # fill group form
        driver.find_element_by_name("group_name").send_keys(name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").send_keys(header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").send_keys(footer)
        # submit group creation
        driver.find_element_by_name("submit").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Выйти").click()

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, name="sdadsadas", header="dsadsadas", footer="dsadsadsa")
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, name="", header="", footer="")
        self.return_to_groups_page(driver)
        self.logout(driver)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
