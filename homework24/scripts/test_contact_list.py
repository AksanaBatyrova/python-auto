"""Homework 24 Add contact"""

from homework24.test_data import login_data, contacts_data
from homework24.pages.login_page import LoginPage
from homework24.pages.contact_list_page import ContactListPage
from homework24.pages.add_contact_page import AddContactPage
from homework24.pages.edit_contact_page import EditContactPage
from homework24.pages.contact_details_page import ContactDetailsPage
from logs.logger import setup_logger

logger = setup_logger(__name__)


def test_login_valid(driver):
    logger.info("Verify that user can be logged in using valid credentials")
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)

    assert 'Contact List App' in login_page.get_page_header()

    login_page.enter_email(login_data.USERNAME_VALID)
    login_page.enter_password(login_data.PASSWORD_VALID)
    login_page.click_submit()

    assert 'Contact List' in contact_list_page.get_page_header()


def test_add_contact_required(driver):
    logger.info("Verify that user can add contact with only required fields")
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)
    add_contact_page = AddContactPage(driver)

    login_page.login(login_data.USERNAME_VALID, login_data.PASSWORD_VALID)

    contact_list_page.get_page_header()
    contact_list_page.click_add_contact_button()

    add_contact_page.fill_first_name(contacts_data.contact_1.first_name)
    add_contact_page.fill_last_name(contacts_data.contact_1.last_name)
    add_contact_page.click_submit_button()
    contact_list_page.wait_for_table_to_load()

    assert (f"{contacts_data.contact_1.first_name} {
               contacts_data.contact_1.last_name}"
            in contact_list_page.get_contact_name(1))


def test_add_contact_full(driver):
    logger.info("Verify that user can add contact with all fields populated")
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)
    add_contact_page = AddContactPage(driver)

    login_page.login(login_data.USERNAME_VALID, login_data.PASSWORD_VALID)

    contact_list_page.get_page_header()
    contact_list_page.click_add_contact_button()

    assert "Add Contact" in add_contact_page.get_page_header()

    add_contact_page.fill_first_name(contacts_data.contact_2.first_name)
    add_contact_page.fill_last_name(contacts_data.contact_2.last_name)
    add_contact_page.fill_birthday(contacts_data.contact_2.birthdate)
    add_contact_page.fill_email(contacts_data.contact_2.email)
    add_contact_page.fill_phone(contacts_data.contact_2.phone)
    add_contact_page.fill_street_1(contacts_data.contact_2.street_1)
    add_contact_page.fill_street_2(contacts_data.contact_2.street_2)
    add_contact_page.fill_city(contacts_data.contact_2.city)
    add_contact_page.fill_state(contacts_data.contact_2.state)
    add_contact_page.fill_postal_code(contacts_data.contact_2.postal_code)
    add_contact_page.fill_country(contacts_data.contact_2.country)
    add_contact_page.click_submit_button()
    contact_list_page.wait_for_table_to_load()

    assert 'Contact List' in contact_list_page.get_page_header()
    assert (f"{contacts_data.contact_2.first_name} {
               contacts_data.contact_2.last_name}"
            in contact_list_page.get_contact_name(1))


def test_edit_contact(driver):
    logger.info("Verify that user can delete contact")
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)
    contact_details_page = ContactDetailsPage(driver)
    add_contact_page = AddContactPage(driver)
    edit_contact_page = EditContactPage(driver)

    login_page.login(login_data.USERNAME_VALID, login_data.PASSWORD_VALID)

    contact_list_page.get_page_header()
    contact_list_page.click_add_contact_button()

    add_contact_page.add_contact_required_only(
        contacts_data.contact_3.first_name,
        contacts_data.contact_3.last_name)
    contact_list_page.wait_for_table_to_load()
    contact_list_page.open_contact_details(1)

    contact_details_page.wait_for_details_to_load()
    contact_details_page.click_edit_contact_button()

    edit_contact_page.wait_edit_form_to_load()
    edit_contact_page.edit_first_name(contacts_data.contact_2.first_name)
    edit_contact_page.edit_last_name(contacts_data.contact_2.last_name)
    edit_contact_page.click_submit_button()

    contact_details_page.wait_for_details_to_load()

    assert (contacts_data.contact_2.first_name
            in contact_details_page.get_contact_firstname())
    assert (contacts_data.contact_2.last_name
            in contact_details_page.get_contact_lastname())


def test_delete_contact(driver):
    logger.info("Verify that user can add contact with only required fields")
    login_page = LoginPage(driver)
    contact_list_page = ContactListPage(driver)
    add_contact_page = AddContactPage(driver)
    contact_details_page = ContactDetailsPage(driver)

    login_page.login(login_data.USERNAME_VALID, login_data.PASSWORD_VALID)
    contact_list_page.wait_for_table_to_load()
    contact_list_page.click_add_contact_button()
    add_contact_page.add_contact_required_only(
        contacts_data.contact_1.first_name,
        contacts_data.contact_1.last_name)
    contact_list_page.wait_for_table_to_load()
    contact_list_page.open_contact_details(1)

    contact_details_page.wait_for_details_to_load()
    contact_details_page.click_delete_contact_button()
    assert ('Are you sure you want to delete this contact?'
            in contact_details_page.get_alert_text())
    contact_details_page.confirm_contact_deletion()

    assert (f"{contacts_data.contact_2.first_name} {
               contacts_data.contact_2.last_name}"
            not in contact_list_page.get_contact_name(1))
