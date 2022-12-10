from RomeNumbers import intToRoman
import unittest

def intToRomanTest(unittest.TestCase):
    # test for numbers
    
    def test(self):
        self.assertEqual(intToRoman(1256, "MCCLVI"))
        self.assertEqual(intToRoman(3521, "MMMDXXI"))
        self.assertEqual(intToRoman(379, "CCCLXXIX"))
        self.assertEqual(intToRoman(899, "DCCCXCIX"))

if __name__ == '__main__':
    unittest.main()