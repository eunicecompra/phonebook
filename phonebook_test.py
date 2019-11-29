import unittest

from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    def test_phonebook_class(self):
        self.assertIsInstance(Phonebook(), Phonebook)


if __name__ == '__main__':
    unittest.main()
