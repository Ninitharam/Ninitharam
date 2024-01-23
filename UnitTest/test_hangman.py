import unittest
from unittest.mock import patch
from hangman import randomWord, spacedOut, hang

class HangmanTestCase(unittest.TestCase):

    def test_randomWord(self):
        # Assuming words.txt contains a list of words
        with patch('builtins.open', side_effect=[['apple', 'banana', 'orange']]):
            word = randomWord()
            self.assertIn(word, ['apple', 'banana', 'orange'])

    def test_spacedOut(self):
        word = 'hangman'
        guessed = ['a', 'n']
        result = spacedOut(word, guessed)
        self.assertEqual(result, '_ a _ _ _ a n ')

    def test_hang_correct_guess(self):
        word = 'hangman'
        guess = 'a'
        result = hang(guess, word)
        self.assertFalse(result)

    def test_hang_incorrect_guess(self):
        word = 'hangman'
        guess = 'z'
        result = hang(guess, word)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
