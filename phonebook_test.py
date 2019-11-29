import unittest
import phonebook

class TestPhonebook(unittest.TestCase):
    def test_phonebook_class(self):
        self.assertIsInstance(phonebook.Phonebook(), phonebook.Phonebook)


if __name__ == '__main__':
    unittest.main()
