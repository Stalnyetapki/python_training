from selenium import webdriver
from fixture.session import SessionHelper
from  fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:/projects/drivers/geckodriver/geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://addressbook:81/group.php")

    def destroy(self):
        self.driver.quit()
