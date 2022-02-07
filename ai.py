# (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.
# This is the Child Class to the Player_Mode Parent which establishes inheritance

from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.gestured_selected = random.choice(self.gestures)
