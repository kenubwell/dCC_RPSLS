#(15 points): As a developer, I want to find a way to properly incorporate inheritance into my game. 
#This is the Child Class to the Player Parent Class which establishes inheritance

from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("Please enter in a player name: ")

    def choose_gesture (self):
        selected_gesture = input(f'Enter in the gesture you want to use: "{self.gesture_list[0]}", "{self.gesture_list[1]}", "{self.gesture_list[2]}", "{self.gesture_list[3]}", "{self.gesture_list[4]}": ')
        if selected_gesture in self.gesture_list:
            self.gesture_selected = selected_gesture
            print('Gesture recorded.')
        else:
            print('Invalid Entry.')
            print('Please make sure to type "Rock" for Rock or "Lizard" for Lizard, as examples (case sensitive).')
            self.choose_gesture()