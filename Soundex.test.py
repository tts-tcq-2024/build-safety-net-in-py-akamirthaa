import unittest
from Soundex import check_format


class TestSoundex(unittest.TestCase):
    def test_name_format(self):
        self.assertEqual(check_format(""), "")
        self.assertEqual(check_format("Robert"),"R163")

    def test_similar_names(self):
        self.assertEqual(check_format("Robert"), "R163")
        self.assertEqual(check_format("Rupert"), "R163")
    
    def test_pad_zeros(self):
        self.assertEqual(check_format("AK"), "A200")
        self.assertEqual(check_format("Dever"), "D160")
    
    def test_names_with_double_letters(self):
        self.assertEqual(check_format("Lloyd"), "L300")
        self.assertEqual(check_format("Gutierrez"), "G362")


    
if __name__ == '__main__':
    unittest.main()
