import unittest

class TestAuth(unittest.TestCase):
    def test_password_in_script(self):
        password = 'supersecret'
        self.assertEqual(password, 'supersecret')

if __name__ == '__main__':
    unittest.main()
