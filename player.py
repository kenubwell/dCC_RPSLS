# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
# a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
# the gesture list is in line 8

# This is a Parent Class to support different types of players
class Player:

    def __init__(self):
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.wins = 0
        self.name = ''
        self.gesture_selected = ''

    def choose_gesture(self):
        pass  # method overide will be used by child classes
