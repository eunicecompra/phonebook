import unittest

from unittest.mock import patch
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    def test_phonebook_class(self):
        self.assertIsInstance(Phonebook(), Phonebook)

    @patch("builtins.input", side_effect=["3"])
    def test_input_size(self, input):
        p = Phonebook()
        p.readInput()
        self.assertEqual(p.size, 3)


if __name__ == '__main__':
    unittest.main()
