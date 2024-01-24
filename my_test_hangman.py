import unittest
from hangman import pygame_helper, randomWord, spacedOut

class HangmanTest(unittest.TestCase):
    def setUp(self):
        pygame_helper.initialize_pygame()

    def tearDown(self):
        pygame_helper.quit_pygame()

    def test_random_word(self):
        word = randomWord()
        # Add assertions to check if the word is valid...

    # Add more tests for other functions...

if __name__ == "__main__":
    unittest.main()
     