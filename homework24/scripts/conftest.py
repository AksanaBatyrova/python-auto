"""Configuration module for tests"""

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from homework24.pages.login_page import LoginPage
from homework24.pages.contact_list_page import ContactListPage
from homework24.pages.contact_details_page import ContactDetailsPage
from homework24.test_data import login_data


@pytest.fixture
def driver():
    base_url = "https://thinking-tester-contact-list.herokuapp.com/"
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.close()


@pytest.fixture(autouse=True)
def clear_all_contacts():
    yield
    base_url = "https://thinking-tester-contact-list.herokuapp.com/"
    driver = webdriver.Chrome()
    driver.get(base_url)
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)
    contact_details_page = ContactDetailsPage(driver)

    login_page.login(login_data.USERNAME_VALID, login_data.PASSWORD_VALID)

    contact_list_page.wait_for_table_to_load()

    def delete_contacts():
        try:
            contact_name = contact_list_page.get_contact_name(1)
            if contact_name != 'No contacts found':
                contact_list_page.open_contact_details(1)
                contact_details_page.wait_for_details_to_load()
                contact_details_page.click_delete_contact_button()
                contact_details_page.confirm_contact_deletion()
                contact_list_page.wait_for_table_to_load()
                delete_contacts()
            else:
                driver.close()
        except TimeoutException:
            driver.close()

    delete_contacts()
