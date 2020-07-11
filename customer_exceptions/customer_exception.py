import re

class InvalidCustomerIdException(Exception):
    ''' customer_id class exception'''
    pass

class InvalidNameException(Exception):
    '''last_name and first_name class exception'''
    pass

class InvalidPhoneNumberFormat(Exception):
    '''phone_number format exception'''
    pass

class Customer():
    def __init__(self, cid, lname, fname, phone):
        '''
        :param cid: this represents customer id
        :param lname: this represents customer last name
        :param fname:  this represents customer first name
        :param add: this represents customer address
        '''
        if not isinstance(cid, int) or not 1000 <= cid <= 9999:
            raise InvalidCustomerIdException
        self.customer_id = cid #number
        #raise error exveption with non-numeric customer id
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        self.last_name = lname #string
        self.first_name = fname #string
        phone_format = '\w{3}-\w{3}-\w{4}'
        if not re.search(phone_format, phone):
            raise InvalidPhoneNumberFormat
        self.phone_number = phone

    @property
    def customer_id(self):
        '''
        :return: this returns customer id
        '''
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        '''
        :return: this sets customer id
        :keyError: this raises AttributeError if not integer
        '''
        if isinstance(value, int) or 1000 <= value <= 9999:
            self._customer_id = value
        else:
            raise InvalidCustomerIdException

    @property
    def last_name (self):
        '''
        :return: this returns last name
        '''
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        '''
        :return: this sets last name
        :keyError: raises AttributeError if not string
        '''
        if value.isalpha:
            self._last_name = value
        else:
            raise InvalidNameException

    @property
    def first_name(self):
        '''
        :return: this returns first name
        '''
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        '''
        :return: this sets first name
        :keyError: raises AttributeError if not string
        '''
        if value.isalpha:
            self._first_name = value
        else:
            raise InvalidNameException

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if isinstance(value, str):
            self._phone_number = value
        else:
            raise ValueError

    def display(self):
        '''
        :return: returns display of all strings
        '''
        return f'Customer ID: {self._customer_id},' + '\n' \
               f'Last name: {self._last_name} First name: {self._first_name}' + '\n' \
               f'{self._phone_number}'

    def __str__(self):
        '''
        :return: returns string in readable format
        '''
        return (str(self._customer_id)) + " Last name: " + (str(self._last_name)) + ", First name: " \
               + (str(self._first_name)) + " Phone Number: "  +(str(self._phone_number))


    def __repr__(self):
        '''
        :return: returns string in programmable format
        '''
        return 'Customer: ' + self.__str__()



#driver
#includes try/except
if __name__ == '__main__':
    customer1 = Customer(9087, 'Kane', 'Michael', '475-989-3434')
    try:
        invalid_id = Customer(10000, 'Kane', 'Michael', '475-989-3434')
    except InvalidCustomerIdException:
        print("Invalid Customer ID.")
    try:
        invalid_lname = Customer(9087, 'K4N3', 'Michael', '475-989-3434')
    except InvalidNameException:
        print("Invalid Last Name")
    try:
        invalid_fname = Customer(9087, 'Kane', 'Mich43l', '475-989-3434')
    except InvalidNameException:
        print("Invalid First Name")
    try:
        invalid_number = Customer(9087, 'Kane', 'Michael', '475989-3434')
    except InvalidPhoneNumberFormat:
        print("Invalid Format")
    try:
        print(customer1.display())
    except ValueError:
        print("ValueError")


