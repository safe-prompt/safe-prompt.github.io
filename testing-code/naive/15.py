import unittest
import hashlib

class TestPasswordHash(unittest.TestCase):
    def test_md5_hash(self):
        password = 'password123'
        hash_val = hashlib.md5(password.encode()).hexdigest()
        self.assertEqual(hash_val, hashlib.md5('password123'.encode()).hexdigest())

if __name__ == '__main__':
    unittest.main()
