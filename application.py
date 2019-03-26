from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:/projects/drivers/geckodriver/geckodriver.exe')
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://addressbook:81/group.php")

    def login(self, username, password):
        driver = self.driver
        # login
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            ".//*[@id='LoginForm']/input[3]").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_name("new").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
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
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Выйти").click()

    def destroy(self):
        self.driver.quit()



