
import unittest
from RunMorse import encrypt
from RunMorse import decrypt


class RunMorseTest(unittest.TestCase):
    

    def test_encrypt(self):
        self.assertEqual(
            encrypt("there is some text"),
            "- .... . .-. . / .. ... / "
            "... --- -- . / - . -..- - ")

    def test_decrypt(self):
        self.assertEqual(
            decrypt(". .-.. -.. -.. .- "
                    "-. ... ..- .-. .. -. "),
            "elddansurin ")

    def test_decrypt1(self):
        self.assertEqual(decrypt(
            "- .... . / -- .- - .-. .. -..- "),
            "the matrix ")


if __name__ == '__main__':
    unittest.main()
