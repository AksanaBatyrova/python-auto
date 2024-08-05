"""Contact List Page module"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from homework24.pages.base_page import BasePage


class ContactListPage(BasePage):
    """ Contact List Page """
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.TAG_NAME, 'h1')
        self.add_contact_button = (By.ID, 'add-contact')
        self.contacts_table = (By.CLASS_NAME, 'contactTable')
        self.table_body = (
            "(//tr[@class='contactTableBodyRow']/td[2])[{row_number}]")

    def wait_for_table_to_load(self):
        return self.wait_for_element(self.contacts_table)

    def get_page_header(self):
        return self.get_text(self.page_header)

    def click_add_contact_button(self):
        self.click(self.add_contact_button)

    def get_contact_name(self, row_number):
        try:
            return self.get_text((By.XPATH, self.table_body.format(
                row_number=row_number)))
        except TimeoutException:
            return 'No contacts found'

    def open_contact_details(self, row_number):
        return self.click(
            (By.XPATH,
             f"(//tr[@class='contactTableBodyRow']/td[2])[{row_number}]"))
