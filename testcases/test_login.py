
from Pageobjects.LoginPage import LoginPage
from utilities.Readconfig import ReadConfig
from utilities.logger import LogGen


class Test001Login:
    base_url = ReadConfig.get_application_url()
    admin_email = ReadConfig.get_admin_email()
    admin_password = ReadConfig.get_admin_password()
    logger = LogGen.log_gen()

    def test_home_page_title(self, setup):
        self.logger.info("Test001Login")
        self.driver = setup
        self.driver.get(self.base_url)
        page_title = self.driver.title
        self.driver.close()
        if page_title == "Your store. Login":
            self.logger.info("Test001Login passed")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
            self.logger.info("Test001Login failed")
            assert False

        print(page_title)

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("test_login started")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_admin_email(self.admin_email)
        self.login_page.set_admin_password(self.admin_password)
        self.login_page.click_login()
        new_page_title = self.driver.title

        if new_page_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("test_login started passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("test_login started failed")
            assert False

        print(new_page_title)


