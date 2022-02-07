#(10 points): As a player, I want the correct player to win a given round based on the choices* made by each player.  
#(10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner. 
from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None
    

    def run_game(self):
        self.display_welcome()
        self.game_type()
        self.game_round()

    def display_welcome(self):
        print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock (RPSLS).')
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
        print('- Spock vaporizes Rock')
        print('The first player to win TWICE wins the Game. \n')
    
    def game_type(self):
        type_of_game = int(input('Choose the type of game. Press "1" for Multiplayer game or Press "2" for Single Player vs. AI: '))
        game_type = False

        while game_type is False:
            if type_of_game == 1 or type_of_game == 2:  
                if type_of_game == 1:
                    self.player2 = Human()
                    self.player1.set_name()
                    print(f'Player 1 is "{self.player1.name}" ') 
                    game_type = True
                elif type_of_game == 2:
                    self.player2 = AI()
                    self.player1.set_name()
                    print(f'Your AI opponent is {self.player2.set_name}')
                    game_type = True   
            elif type_of_game != 1 or type_of_game != 2:  
                print('Invalid Entry.')
                type_of_game = int(input('Choose the type of game. Press "1" for Multiplayer game or Press "2" for Single Player vs. AI: '))

    
    def game_round(self):

        while self.player1.wins < 2 and self.player2.wins < 2:
            print('\nCurrent Round')
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            
            if self.player1.gesture_selected == self.player2.gesture_selected:
                print('This Round is a tie')

            elif self.player1.gesture_selected == self.player1.gesture_list[0] and self.player2.gesture_selected == self.player2.gesture_list[2]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.gesture_selected == self.player1.gesture_list[0] and self.player2.gesture_selected == self.player2.gesture_list[3]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.gesture_selected == self.player1.gesture_list[2] and self.player2.gesture_selected == self.player2.gesture_list[1]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[2] and self.player2.gesture_selected == self.player2.gesture_list[3]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[1] and self.player2.gesture_selected == self.player2.gesture_list[0]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[1] and self.player2.gesture_selected == self.player2.gesture_list[4]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[3] and self.player2.gesture_selected == self.player2.gesture_list[4]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[3] and self.player2.gesture_selected == self.player2.gesture_list[1]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[4] and self.player2.gesture_selected == self.player2.gesture_list[2]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
            elif self.player1.choose_gesture() == self.player1.gesture_list[4] and self.player2.gesture_selected == self.player2.gesture_list[0]:
                self.player1.wins += 1
                print(f'{self.player1.name} won this round.')
          
        

    
    def display_winner(self):
        pass

    