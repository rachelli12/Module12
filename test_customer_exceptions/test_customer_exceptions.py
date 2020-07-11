import unittest
from customer_exceptions import customer_exception as ce
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer_id = 9087
        self.lname = 'Kane'
        self.fname = 'Michael'
        self.phone_number = '475-989-3434'
        self.customer = ce.Customer(9087,'Kane', 'Michael', '475-989-3434')

    def tearDown(self):
        del self.customer

    def test_object_required_attributes(self):
        #constructor with valid attributes
        self.assertEqual(self.customer.customer_id, 9087)
        self.assertEqual(self.customer.last_name, 'Kane')
        self.assertEqual(self.customer.first_name, 'Michael')
        self.assertEqual(self.customer.phone_number, '475-989-3434')

    def test_invalid_customer_id(self):
        with self.assertRaises(ce.InvalidCustomerIdException):
            c = ce.Customer(10000, 'Kane', 'Michael', '475-989-3434')

    def test_invalid_last_name(self):
        with self.assertRaises(ce.InvalidNameException):
            c = ce.Customer(9087,'K4N3', 'Michael', '475-989-3434')

    def test_invalid_first_name(self):
        with self.assertRaises(ce.InvalidNameException):
            c = ce.Customer(9087,'Kane', 'Mich43l', '475-989-3434')

    def test_invalid_phone_number(self):
        with self.assertRaises(ce.InvalidPhoneNumberFormat):
            c = ce.Customer(9087,'Kane', 'Michael', '475989-3434')






