#(15 points): As a developer, I want to find a way to properly incorporate inheritance into my game. 
    #This is the Child Class to the Player Parent Class which establishes inheritance
#(5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
    #lines 25 and 46 for input validation (if/else conditional)

from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("Please enter in a player name: ")

    def choose_gesture (self):
        gestured_confirmed = False
        print(f'Enter in "0" for {self.gesture_list[0]}')
        print(f'Enter in "1" for {self.gesture_list[1]}')
        print(f'Enter in "2" for {self.gesture_list[2]}')
        print(f'Enter in "3" for {self.gesture_list[3]}')
        print(f'Enter in "4" for {self.gesture_list[4]}')
        
        while gestured_confirmed is False:
            selected_gesture = int(input('Enter in the number (gesture) you want to use: '))
            if selected_gesture >= 0 and selected_gesture <= 4:
                if selected_gesture == 0:
                    self.gesture_selected = self.gesture_list[0]
                    print('Gesture recorded.')
                    gestured_confirmed = True
                elif selected_gesture == 1:
                    self.gesture_selected = self.gesture_list[1]
                    print('Gesture recorded.')
                    gestured_confirmed = True
                elif selected_gesture == 2:
                    self.gesture_selected = self.gesture_list[2]
                    print('Gesture recorded.')
                    gestured_confirmed = True
                elif selected_gesture == 3:
                    self.gesture_selected = self.gesture_list[3]
                    print('Gesture recorded.')
                    gestured_confirmed = True
                elif selected_gesture == 4:
                    self.gesture_selected = self.gesture_list[4]
                    print('Gesture recorded.')
                    gestured_confirmed = True
            else:
                print('Invalid Entry.')
                print('Please make sure to type a number between "0" and "4" per instructions above.')
                