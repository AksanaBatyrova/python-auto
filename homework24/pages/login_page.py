"""Login Page module"""

from selenium.webdriver.common.by import By
from homework24.pages.base_page import BasePage


class LoginPage(BasePage):
    """ Contact List App Login Page """
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.TAG_NAME, 'h1')
        self.login_email_input = (By.ID, 'email')
        self.login_password_input = (By.ID, 'password')
        self.login_submit_button = (By.ID, 'submit')
        self.login_error_message = (By.ID, 'error')

    def get_page_header(self):
        return self.get_text(self.page_header)

    def enter_email(self, username):
        self.fill(self.login_email_input, username)

    def enter_password(self, password):
        self.fill(self.login_password_input, password)

    def click_submit(self):
        self.click(self.login_submit_button)

    def login(self, username, password):
        self.enter_email(username)
        self.enter_password(password)
        self.click_submit()
