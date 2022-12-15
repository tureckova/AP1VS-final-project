"""Unit testy."""

import unittest
from main import cleared_text
from main import all_letters
from main import most_frequent_letter
from main import least_frequent_letter
from main import average_letter_frequency
from main import appereance_of_every_letter
from main import __name__


class TestCountLetters(unittest.TestCase):
    """Třída na unit testy."""
    def test_cleared_text(self):
        """
        Unit test pro funkci cleared_text().

        :param self:
        """
        self.assertEqual(cleared_text("Ahoj jak se máš"), "ahojjaksemas")
        self.assertEqual(cleared_text(
            "Test čištění textu"), "testcistenitextu")
        self.assertNotEqual(cleared_text("Test čištění textu"), "ahojjaksemas")

    def test_all_letters(self):
        """
        Unit test pro funkci all_letters().

        :param self:
        """
        self.assertEqual(all_letters(cleared_text(
            "Ahoj jak se máš")), 12)
        self.assertEqual(all_letters(cleared_text(
            "Druhý test")), 9)
        self.assertNotEqual(all_letters(cleared_text(
            "Kolik znaků tu je?")), 5)

    def test_most_frequent_letter(self):
        """
        Unit test pro funkci most_frequent_letter().

        :param self:
        """
        self.assertEqual(most_frequent_letter(cleared_text(
            "Ahoj jak se máš")), ('a', 3))
        self.assertEqual(most_frequent_letter(cleared_text(
            "Druhý test")), ('t', 2))
        self.assertNotEqual(most_frequent_letter(cleared_text(
            "Ahoj jak se máš")), ('q', 4))

    def test_least_frequent_letter(self):
        """
        Unit test pro funkci least_frequent_letter().

        :param self:
        """
        self.assertEqual(least_frequent_letter(cleared_text(
            "Ahoj jak se máš")), ('m', 1))
        self.assertEqual(least_frequent_letter(cleared_text(
            "Druhý test")), ('s', 1))
        self.assertNotEqual(least_frequent_letter(cleared_text(
            "Ahoj jak se máš")), ('r', 2))

    def test_average_letter_frequency(self):
        """
        Unit test pro funkci average_letter_frequency().

        :param self:
        """
        self.assertEqual(average_letter_frequency(cleared_text(
            "Ahoj jak se máš")), 1.0)
        self.assertEqual(average_letter_frequency(cleared_text(
            "Ahoj, jak se máš?!")), 0.8)
        self.assertNotEqual(average_letter_frequency(cleared_text(
            "Ahoj!")), 1.0)

    def test_appereance_of_every_letter(self):
        """
        Unit test pro funkci appereance_of_every_letter().

        :param self:
        """
        self.assertEqual(appereance_of_every_letter(cleared_text(
            "ahojjaksemas")), {'a': 3, 'e': 1, 'h': 1, 'j': 2,
                               'k': 1, 'm': 1, 'o': 1, 's': 2})
        self.assertEqual(appereance_of_every_letter(cleared_text(
            "druhytestznaku")),
                         {'a': 1, 'd': 1, 'e': 1, 'h': 1, 'k': 1,
                          'n': 1, 'r': 1, 's': 1, 't': 2,
                          'u': 2, 'y': 1, 'z': 1})
        self.assertNotEqual(appereance_of_every_letter(cleared_text(
            "ahojjaksemas")), {'a': 3})


if __name__ == '__main__':
    unittest.main()
