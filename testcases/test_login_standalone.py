from selenium import webdriver
import pytest
from Pageobjects.LoginPage import LoginPage


class Test001Login:
    base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    admin_email = "admin@yourstore.com"
    admin_password = "admin"

    def test_home_page_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        page_title = self.driver.title
        self.driver.close()
        if page_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_admin_email(self.admin_email)
        self.login_page.set_admin_password(self.admin_password)
        self.login_page.click_login()
        new_page_title = self.driver.title

        if new_page_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
