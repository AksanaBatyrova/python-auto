"""Edit Contact Page module"""

from selenium.webdriver.common.by import By
from homework24.pages.base_page import BasePage


class EditContactPage(BasePage):
    """ Edit Contact Page """
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.TAG_NAME, 'h1')
        self.edit_contact_form = (By.ID, 'edit-contact')
        self.edit_firstname_input = (
            By.CSS_SELECTOR, '#edit-contact #firstName')
        self.edit_lastname_input = (By.CSS_SELECTOR, '#edit-contact #lastName')
        self.edit_birthdate_input = (
            By.CSS_SELECTOR, '#edit-contact #birthdate')
        self.edit_email_input = (By.CSS_SELECTOR, '#edit-contact #email')
        self.edit_phone_input = (By.CSS_SELECTOR, '#edit-contact #phone')
        self.edit_street1_input = (By.CSS_SELECTOR, '#edit-contact #street1')
        self.edit_street2_input = (By.CSS_SELECTOR, '#edit-contact #street2')
        self.edit_city_input = (By.CSS_SELECTOR, '#edit-contact #city')
        self.edit_state_input = (
            By.CSS_SELECTOR, '#edit-contact #stateProvince')
        self.edit_postcode_input = (
            By.CSS_SELECTOR, '#edit-contact #postalCode')
        self.edit_country_input = (By.CSS_SELECTOR, '#edit-contact #country')
        self.edit_contact_submit_button = (By.ID, 'submit')

    def get_page_header(self):
        return self.get_text(self.page_header)

    def wait_edit_form_to_load(self):
        return self.wait_for_element(self.edit_contact_form)

    def edit_first_name(self, first_name):
        self.find(self.edit_firstname_input)
        self.clear(self.edit_firstname_input)
        self.fill(self.edit_firstname_input, first_name)

    def edit_last_name(self, last_name):
        self.find(self.edit_lastname_input)
        self.clear(self.edit_lastname_input)
        self.fill(self.edit_lastname_input, last_name)

    def edit_birthday(self, birthdate):
        self.fill(self.edit_birthdate_input, birthdate)

    def edit_email(self, email):
        self.fill(self.edit_email_input, email)

    def edit_phone(self, phone):
        self.fill(self.edit_phone_input, phone)

    def edit_street_1(self, street_1):
        self.fill(self.edit_street1_input, street_1)

    def edit_street_2(self, street_2):
        self.fill(self.edit_street2_input, street_2)

    def edit_city(self, city):
        self.fill(self.edit_city_input, city)

    def edit_state(self, state):
        self.fill(self.edit_state_input, state)

    def edit_postal_code(self, postal_code):
        self.fill(self.edit_postcode_input, postal_code)

    def edit_country(self, country):
        self.fill(self.edit_country_input, country)

    def click_submit_button(self):
        self.click(self.edit_contact_submit_button)

    def edit_contact_required_only(self, first_name, last_name):
        self.edit_first_name(first_name)
        self.edit_last_name(last_name)
        self.click_submit_button()

    def edit_contact_full(self, first_name, last_name, birthdate, email, phone,
                          street_1, street_2, city, state, postal_code,
                          country):
        self.edit_first_name(first_name)
        self.edit_last_name(last_name)
        self.edit_birthday(birthdate)
        self.edit_email(email)
        self.edit_phone(phone)
        self.edit_street_1(street_1)
        self.edit_street_2(street_2)
        self.edit_city(city)
        self.edit_state(state)
        self.edit_postal_code(postal_code)
        self.edit_country(country)
        self.click_submit_button()
