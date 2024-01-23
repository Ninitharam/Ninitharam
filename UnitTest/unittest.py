import unittest


class HangmanTest(unittest.TestCase):

    def test_hang_correct_guess(self):
        word = "python"
        guess = "p"
        self.assertFalse(hang(guess, word), "Correct guess should return False")

    def test_hang_incorrect_guess(self):
        word = "python"
        guess = "z"
        self.assertTrue(hang(guess, word), "Incorrect guess should return True")

    def test_spacedOut_no_guesses(self):
        word = "python rocks"
        self.assertEqual(spacedOut(word), "_ _ _ _ _ _   _ _ _ _ _", "Initial spacedOut should have underscores")

    def test_spacedOut_with_guesses(self):
        word = "python rocks"
        guessed = ['p', 'o', 'r']
        self.assertEqual(spacedOut(word, guessed), "P _ _ _ _ _   R o _ _ _", "Incorrectly guessed letters should be revealed")

    def test_randomWord(self):
        # Mocking random.choice to always return a known word for testing
        with patch('random.choice', side_effect=lambda x: x[0][0]):
            word = randomWord()
            self.assertEqual(word, "apple", "randomWord should return a known word")

if __name__ == '__main__':
    unittest.main()
