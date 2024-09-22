import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_repeating_character(self):
        self.assertEqual(generate_soundex("Hermann"),"H655")

    def test_lowercase(self):
        self.assertEqual(generate_soundex("a"),"A000")

    def test_numbers(self):
        self.assertEqual(generate_soundex("James123"), "J520")
    
if __name__ == '__main__':
    unittest.main()
