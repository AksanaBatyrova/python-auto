"""Contact Details Page module"""

from selenium.webdriver.common.by import By
from homework24.pages.base_page import BasePage


class ContactDetailsPage(BasePage):
    """ Add Contact Page """
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.TAG_NAME, 'h1')
        self.contact_details = (By.ID, 'contactDetails')
        self.edit_contact_button = (By.ID, 'edit-contact')
        self.delete_contact_button = (By.ID, 'delete')
        self.contact_firstname = (
            By.CSS_SELECTOR, '#contactDetails #firstName')
        self.contact_lastname = (By.CSS_SELECTOR, '#contactDetails #lastName')

    def get_page_header(self):
        return self.get_text(self.page_header)

    def wait_for_details_to_load(self):
        return self.wait_for_element(self.contact_details)

    def get_contact_firstname(self):
        return self.get_text(self.contact_firstname)

    def get_contact_lastname(self):
        return self.get_text(self.contact_lastname)

    def click_edit_contact_button(self):
        self.click(self.edit_contact_button)

    def click_delete_contact_button(self):
        self.click(self.delete_contact_button)

    def get_alert_text(self):
        return self.get_alert().text

    def confirm_contact_deletion(self):
        self.accept_alert()
