from app.models import User
import unittest

class user_test(unittest.TestCase):
    '''
    setup creates a new instance of the class User and passes in a password of value banana
    the test test_password_setter asserts/confirms that there's a vlaue present after the password is hashed
    the test test_no_access_passwordascertains that the users do not gain any acces o the password as it would be catastrophic
    test_password_verifcation also makes use of the test_password_setter_ as it hashes the password and checks if  it matches the password given
    '''
    def setUp(self):
        self.new_user = User(password='banana')

    def test_password_setter(self):
       self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('banana'))


if __name__ == '__main__':
    unittest.main()