import unittest
from Soundex import generate_final_soundex
from Soundex import add_zeros
from Soundex import four_characters
from Soundex import initial_soundex
from Soundex import drop_letters
from Soundex import get_first_letter

class TestSoundex(unittest.TestCase):
    def test_string_format(self):
        self.assertEqual(generate_final_soundex(""), "No Characters found")
        self.assertEqual(generate_final_soundex("1234"),"No Characters found")
    
    def test_first_letter(self):
        self.assertEqual(get_first_letter("tchebycheff"), "T")
        self.assertEqual(get_first_letter("TCHEBYCHEFF"), "T")

    def test_drop_letters(self):
        self.assertEqual(drop_letters("tchebycheff"),"tcbcff" )
    
    def test_initial_soundex(self):
        self.assertEqual(initial_soundex("tchebycheff"),"T21211")

    def test_four_characters(self):
        self.assertEqual(four_characters("T21211"),"T212")
        self.assertEqual(four_characters("T12"),"T12")
    
    def test_add_zeros(self):
        self.assertEqual(add_zeros("T212"),"T212")
        self.assertEqual(add_zeros("T2"),"T200")

    def test_similar_words(self):
        self.assertEqual(generate_final_soundex("Robert"),'R163')
        self.assertEqual(generate_final_soundex("Rupert"),"R163")

    
if __name__ == '__main__':
    unittest.main()
