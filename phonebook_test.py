import unittest

from unittest.mock import patch
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    test_data = [
        "3",
        "sam 99912222",
        "tom 11122222",
        "harry 12299933"
    ]

    def test_phonebook_class(self):
        self.assertIsInstance(Phonebook(), Phonebook)

    @patch("builtins.input", side_effect=test_data)
    def test_input_details(self, input):
        p = Phonebook()
        p.readInput()
        self.assertEqual(p.size, 3)
        self.assertDictEqual(p.phonebook, dict(sam="99912222", tom="11122222", harry="12299933"))


if __name__ == '__main__':
    unittest.main()
