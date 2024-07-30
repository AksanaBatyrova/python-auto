"""Homework23. Selenium locators"""

# Вам необходимо создать пару контактов, обновить их и удалить через сайт
# https://thinking-tester-contact-list.herokuapp.com/. Для этого необходимо
# пройти все шаги вручную и подобрать все уникальные селекторы с которыми вы
# будите взаимодействовать в процессе работы:

# Экран логина:

# Ввод имени пользователя
# Ввод пароля
# Нажате кнопки 'Login'
# Добавить новый контакт:

# Нажать на кнопку "Add a New Contact": ..
# и тд.
# Результатом Вашей работы должны быть детальные шаги(инструкция) по
# добавлению, обновлению и удалению контактов. Оформите их в файле и
# сделайте PR.


# --LOGIN PAGE--
# 1. Enter login
login_email_input = "#email",
# 2. Enter password
login_password_input = "#password",
# 3. Click submit button
login_submit_button = "#submit",


# --CONTACTS LIST PAGE--
# 4. Click 'Add a New Contact' button
add_contact_button = "#add-contact",

# --ADD CONTACT PAGE--
# 5. Fill necessary fields
add_firstname_input = "#add-contact #firstName",
add_lastname_input = "#add-contact #lastName",
add_birthdate_input = "#add-contact #birthdate",
add_email_input = "#add-contact #email",
add_phone_input = "#add-contact #phone",
add_street1_input = "#add-contact #street1",
add_street2_input = "#add-contact #street2",
add_city_input = "#add-contact #city",
add_stateProvince_input = "#add-contact #stateProvince",
add_postalCode_input = "#add-contact #postalCode",
add_country_input = "#add-contact #country",
# 6. Save contact
add_submit_button = "#submit",

# 7. Create one more contact (fill only necessary fields)
add_contact_button,
add_firstname_input,
add_lastname_input,
add_submit_button

# --CONTACTS LIST PAGE--
# 7. Click at created contact row
contacts_first_row = "//tr[@class='contactTableBodyRow'][1]",


# --SELECTED CONTACT PAGE--
# 8. Click 'Edit Contact' button
edit_contact_button = "#edit-contact",


# --EDIT CONTACT PAGE--
# 9. Edit necessary fields
edit_firstname_input = "#edit-contact #firstName",
edit_lastname_input = "#edit-contact #lastName",
# 10. Save changes
edit_submit_button = "#submit",


# --SELECTED CONTACT PAGE--
# 11. Click 'Return to Contact List' button
delete_contact_button = "#delete",
return_to_contacts_button = "#return",


# --CONTACTS LIST PAGE--
# 12. Select second contact by name
contacts_first_contact_name = "//tr[@class='contactTableBodyRow']/td[.='{firstname} {lastname}']",

# --SELECTED CONTACT PAGE--
# 13. Click 'Delete contact' button
delete_contact_button = "#delete"

# 14. Approve deletion