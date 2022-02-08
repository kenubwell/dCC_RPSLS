#(15 points): As a developer, I want to find a way to properly incorporate inheritance into my game. 
#This is the Child Class to the Player Parent Class which establishes inheritance

from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        self.choose_gesture()

    def set_name(self):
        self.name = 'SkyNet'
    
    def choose_gesture(self):
        selected_gesture = random.choice(self.gesture_list)
        self.gesture_selected = selected_gesture

