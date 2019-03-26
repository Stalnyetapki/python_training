# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/projects/drivers/geckodriver/geckodriver.exe')
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://addressbook:81/group.php")

    def login(self, driver, username, password):
        # login
        self.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            ".//*[@id='LoginForm']/input[3]").click()

    def open_groups_page(self, driver):
        driver.find_element_by_name("new").click()

    def create_group(self, driver, group):
        self.open_groups_page(driver)
        # init group creation
        driver.find_element_by_name("group_name").click()
        # fill group form
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page(driver)

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Выйти").click()

    def test_add_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="sdadsadas", header="dsadsadas", footer="dsadsadsa"))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="", header="", footer=""))
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
