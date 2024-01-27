import time

from Pageobjects.LoginPage import LoginPage
from utilities.Readconfig import ReadConfig
from utilities.logger import LogGen
from utilities import Excellutils


class Test002Login:
    base_url = ReadConfig.get_application_url()
    path = ".//Testdata/Datadriven_Testdata.xlsx"
    logger = LogGen.log_gen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("test_login data driven started")
        self.login_page = LoginPage(self.driver)
        self.rows = Excellutils.get_row_count(self.path, 'Sheet1')
        print("number of rows", self.rows)

        list_status = []

        for r in range(2, self.rows + 1):
            self.admin_email = Excellutils.read_data(self.path, 'Sheet1', r, 1)
            self.admin_password = Excellutils.read_data(self.path, 'Sheet1', r, 2)
            self.expected = Excellutils.read_data(self.path, 'Sheet1', r, 3)
            self.login_page.set_admin_email(self.admin_email)
            self.login_page.set_admin_password(self.admin_password)
            self.login_page.click_login()
            time.sleep(3)
            actual_page_title = self.driver.title
            expected_page_title = "Dashboard / nopCommerce administration"
            print(actual_page_title)

            if actual_page_title == expected_page_title:
                time.sleep(3)
                if self.expected == "Pass":
                    time.sleep(3)
                    self.logger.info("test_login dd passed")
                    self.login_page.click_logout()
                    list_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("test_login dd Failed")
                    self.login_page.click_logout()
                    list_status.append("Fail")

            elif actual_page_title != expected_page_title:
                if self.expected == "Pass":
                    self.logger.info("test_login dd Failed")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("test_login dd Passed")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("Login dd passed")
            self.driver.close()
            assert True
        else:
            self.logger.infor("Login dd failed")
            self.driver.close()
            assert False
        print("list_status array = ")
        print(list_status)
