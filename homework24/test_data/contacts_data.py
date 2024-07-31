"""Module Contacts data"""


class Contact():
    """ Class for defining Contact data """
    def __init__(self, first_name, last_name, birthdate, email, phone,
                 street_1, street_2, city, state, postal_code, country):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.street_1 = street_1
        self.street_2 = street_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country


contact_1 = Contact('John', 'Smith', '23/04/1965', 'john.smith@test.com',
                    '+55512345679', 'Bridge st. 15', '123', 'London', 'London',
                    '123458', 'Great Britain')

contact_2 = Contact('Jane', 'Smith', '14/09/1967', 'jane.smith@test.com',
                    '+55512312345', 'Bridge st. 15', '123', 'London', 'London',
                    '123458', 'Great Britain')

contact_3 = Contact('Betty', 'Smith', '12/09/1992', 'betty.smith@test.com',
                    '+55512345999', 'Bridge st. 15', '123', 'London', 'London',
                    '123458', 'Great Britain')
