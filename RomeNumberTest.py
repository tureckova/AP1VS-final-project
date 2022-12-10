from RomeNumbers import intToRoman
import unittest

class intToRomanTest():

     def test_intoroman(self):
        self.assertEqual(intToRoman(1256, "MCCLVI"))
        self.assertEqual(intToRoman(3521, "MMMDXXI"))
        self.assertEqual(intToRoman(379, "CCCLXXIX"))
        self.assertEqual(intToRoman(899, "DCCCXCIX"))

    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000)
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)
    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, -1)
    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(roman1.NotIntegerError, roman1.to_roman, 0.5)
    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)
    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)
class RoundtripCheck():
    def test_roundtrip(self):
        '''from_roman(to_roman(n))==n for all n'''
        for integer in range(1, 4000):
            numeral = roman1.to_roman(integer)
            result = roman1.from_roman(numeral)
            self.assertEqual(integer, result)

if name == 'main':
    unittest.main()