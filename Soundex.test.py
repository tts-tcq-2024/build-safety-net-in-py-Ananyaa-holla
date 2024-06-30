import unittest
from Soundex import generate_soundex
from Soundex import encode_name

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_encode_name(self):
        self.assertEqual(encode_name("Aeiou","A",0),"A000")

    
if __name__ == '__main__':
    unittest.main()
