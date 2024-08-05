"""Add Contact Page module"""

from selenium.webdriver.common.by import By
from homework24.pages.base_page import BasePage


class AddContactPage(BasePage):
    """ Add Contact Page """
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.TAG_NAME, 'h1')
        self.add_firstname_input = (By.CSS_SELECTOR, '#add-contact #firstName')
        self.add_lastname_input = (By.CSS_SELECTOR, '#add-contact #lastName')
        self.add_birthdate_input = (By.CSS_SELECTOR, '#add-contact #birthdate')
        self.add_email_input = (By.CSS_SELECTOR, '#add-contact #email')
        self.add_phone_input = (By.CSS_SELECTOR, '#add-contact #phone')
        self.add_street1_input = (By.CSS_SELECTOR, '#add-contact #street1')
        self.add_street2_input = (By.CSS_SELECTOR, '#add-contact #street2')
        self.add_city_input = (By.CSS_SELECTOR, '#add-contact #city')
        self.add_state_input = (By.CSS_SELECTOR, '#add-contact #stateProvince')
        self.add_postcode_input = (By.CSS_SELECTOR, '#add-contact #postalCode')
        self.add_country_input = (By.CSS_SELECTOR, '#add-contact #country')
        self.add_contact_submit_button = (By.ID, 'submit')

    def get_page_header(self):
        return self.get_text(self.page_header)

    def fill_first_name(self, first_name):
        self.fill(self.add_firstname_input, first_name)

    def fill_last_name(self, last_name):
        self.fill(self.add_lastname_input, last_name)

    def fill_birthday(self, birthdate):
        self.fill(self.add_birthdate_input, birthdate)

    def fill_email(self, email):
        self.fill(self.add_email_input, email)

    def fill_phone(self, phone):
        self.fill(self.add_phone_input, phone)

    def fill_street_1(self, street_1):
        self.fill(self.add_street1_input, street_1)

    def fill_street_2(self, street_2):
        self.fill(self.add_street2_input, street_2)

    def fill_city(self, city):
        self.fill(self.add_city_input, city)

    def fill_state(self, state):
        self.fill(self.add_state_input, state)

    def fill_postal_code(self, postal_code):
        self.fill(self.add_postcode_input, postal_code)

    def fill_country(self, country):
        self.fill(self.add_country_input, country)

    def click_submit_button(self):
        self.click(self.add_contact_submit_button)

    def add_contact_required_only(self, first_name, last_name):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.click_submit_button()

    def add_contact_full(self, first_name, last_name, birthdate, email, phone,
                         street_1, street_2, city, state, postal_code,
                         country):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_birthday(birthdate)
        self.fill_email(email)
        self.fill_phone(phone)
        self.fill_street_1(street_1)
        self.fill_street_2(street_2)
        self.fill_city(city)
        self.fill_state(state)
        self.fill_postal_code(postal_code)
        self.fill_country(country)
        self.click_submit_button()
