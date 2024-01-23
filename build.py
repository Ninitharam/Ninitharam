#BUILD MANAGEMENT EXAMPLE FOR FLOWERS GAME 

import random
from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")

default_task = "publish"

class FlowersGame:
    def __init__(self):
        self.flowers = ["rose", "tulip", "daisy", "sunflower", "lily"]
        self.selected_flower = random.choice(self.flowers)
        self.guesses_left = 3

    def make_guess(self, guess):
        guess = guess.lower()

        if guess == self.selected_flower:
            return "Congratulations! You guessed the flower."

        self.guesses_left -= 1

        if self.guesses_left == 0:
            return f"Sorry, you ran out of guesses. The flower was {self.selected_flower}."

        return f"Incorrect guess. You have {self.guesses_left} guesses left."

