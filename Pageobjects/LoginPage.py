from selenium.webdriver.common.by import By


class LoginPage:
    textbox_admin_email_by_id = "Email"
    textbox_admin_password_by_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_xpath = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_admin_email(self, admin_email):
        # self.driver.find_element_by_id(self.textbox_admin_email_by_id).clear()
        # self.driver.find_element_by_id(self.textbox_admin_email_by_id).send_keys(admin_email)
        self.driver.find_element(By.ID, self.textbox_admin_email_by_id).clear()
        self.driver.find_element(By.ID, self.textbox_admin_email_by_id).send_keys(admin_email)

    def set_admin_password(self, admin_password):
        # self.driver.find_element_by_id(self.textbox_admin_password_by_id).clear()
        # self.driver.find_element_by_id(self.textbox_admin_password_by_id).send_keys(admin_password)
        self.driver.find_element(By.ID, self.textbox_admin_password_by_id).clear()
        self.driver.find_element(By.ID, self.textbox_admin_password_by_id).send_keys(admin_password)

    def click_login(self):
        # self.driver.find_element_by_xpath(self.button_login_xpath).click()
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        # self.driver.find_element_by_link_text(self.link_logout_link_text).click()
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

