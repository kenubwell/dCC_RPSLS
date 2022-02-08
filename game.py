#(10 points): As a player, I want the correct player to win a given round based on the choices* made by each player.  
#(10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner. 
#(10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.  
#(5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
    #Lines 41 and 55 for input validation (if/elif conditional)

from human import Human
from ai import AI
import time

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None

    def run_game(self):
        self.display_welcome()
        self.game_type()
        self.game_round()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock (RPSLS).')
        print('Each game will be the best of three rounds a.k.a. first player to win TWICE.')
        print('The following are the rules of the game:')
        print('- Rock crushes Scissors')
        print('- Scissors cuts Paper')
        print('- Paper covers Rock')
        print('- Rock crushes Lizard')
        print('- Lizard poisons Spock')
        print('- Spock smashes Scissors')
        print('- Scissors decapitates Lizard')
        print('- Lizard eats Paper')
        print('- Paper disproves Spock')
        print('- Spock vaporizes Rock\n')
    
    def game_type(self):
        type_of_game = int(input('Enter in the game type. Press "1" for Single Player (versus AI) || or Press "2" for Multiplayer game: '))
        game_type = False

        while game_type is False:
            if type_of_game == 1 or type_of_game == 2:  
                if type_of_game == 1:
                    self.player2 = AI()
                    self.player1.set_name()
                    print(f'\nIt will be Player 1 "{self.player1.name}" versus AI opponent "{self.player2.name}".  Good Luck!')
                    game_type = True
                elif type_of_game == 2:
                    self.player2 = Human()
                    self.player1.set_name()
                    print(f'Player 1 is set for "{self.player1.name}"')
                    self.player2.set_name()
                    print(f'\nIt will be Player 1 "{self.player1.name}" versus Player 2 "{self.player2.name}".  Have Fun!')
                    game_type = True   
            elif type_of_game != 1 or type_of_game != 2:  
                print('Invalid Entry.')
                type_of_game = int(input('Choose the type of Game. Press "1" for Single Player (versus AI) || or Press "2" for Multiplayer game: '))

    
    def game_round(self):

        round_count = 1
            
        while self.player1.wins < 2 and self.player2.wins < 2:
            
            time.sleep(1)
            print(f"\nCurrent Round is 'Round {round_count}'")
            self.player1.choose_gesture()
            self.player2.choose_gesture()
     
            if self.player1.gesture_selected == self.player2.gesture_selected:
                print(f"This Round is a tie you both had '{self.player2.gesture_selected}'.")
                round_count += 1

            elif self.player1.gesture_selected == self.player1.gesture_list[0] and self.player2.gesture_selected == self.player2.gesture_list[2]:
                self.player1.wins += 1
                round_count += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[0]}' over {self.player2.name}'s '{self.player2.gesture_list[2]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[0] and self.player2.gesture_selected == self.player2.gesture_list[3]:
                self.player1.wins += 1
                round_count += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[0]}' over {self.player2.name}'s '{self.player2.gesture_list[3]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[2] and self.player2.gesture_selected == self.player2.gesture_list[1]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[2]}' over {self.player2.name}'s '{self.player2.gesture_list[1]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[2] and self.player2.gesture_selected == self.player2.gesture_list[3]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[2]}' over {self.player2.name}'s '{self.player2.gesture_list[3]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[1] and self.player2.gesture_selected == self.player2.gesture_list[0]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[1]}' over {self.player2.name}'s '{self.player2.gesture_list[0]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[1] and self.player2.gesture_selected == self.player2.gesture_list[4]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[1]}' over {self.player2.name}'s '{self.player2.gesture_list[4]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[3] and self.player2.gesture_selected == self.player2.gesture_list[4]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[3]}' over {self.player2.name}'s '{self.player2.gesture_list[4]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[3] and self.player2.gesture_selected == self.player2.gesture_list[1]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[3]}' over {self.player2.name}'s '{self.player2.gesture_list[1]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[4] and self.player2.gesture_selected == self.player2.gesture_list[2]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[4]}' over {self.player2.name}'s '{self.player2.gesture_list[2]}'.")
            elif self.player1.gesture_selected == self.player1.gesture_list[4] and self.player2.gesture_selected == self.player2.gesture_list[0]:
                round_count += 1
                self.player1.wins += 1
                print(f"{self.player1.name} won this round by having gestured '{self.player1.gesture_list[4]}' over {self.player2.name}'s '{self.player2.gesture_list[0]}'.")
            else:
                round_count += 1
                self.player2.wins += 1
                print(f"{self.player2.name} won this round by having '{self.player2.gesture_selected}' over {self.player1.name}'s '{self.player1.gesture_selected}'.")

    
    def display_winner(self):
        if self.player1.wins == 2:
            print(f'\n{self.player1.name} wins the game!')
            print(f'Summary of the game: The Winner "{self.player1.name}" had {self.player1.wins} wins || The Loser "{self.player2.name}" had {self.player2.wins} win(s)\n')
        elif self.player2.wins == 2:
            print(f'\n{self.player2.name} wins the game!')
            print(f'Summary of the game: The Winner "{self.player2.name}" had {self.player2.wins} wins || The Loser "{self.player1.name}" had {self.player1.wins} win(s)\n')

    




