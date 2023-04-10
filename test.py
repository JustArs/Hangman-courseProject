import unittest
from HangmanTerm import HangmanTerm


class WordsTest(unittest.TestCase):
    def test_FirstWord(self):
        
        result = HangmanTerm
        self.assertEqual(result, result, "No!")


