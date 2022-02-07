# (10 points): As a player, I want the correct player to win a given round based on the choices* made by each player.
# (10 points): As a player, I want the game of RPSLS to be at minimum a 'best of three' to decide a winner.
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None

    def run_game(self):
        self.display_welcome()
        self.game_type()

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
        type_of_game = int(input(
            'Choose the type of game. Press "1" for Multiplayer game or Press "2" for Single Player vs. AI: '))
        game_type = False

        while game_type is False:
            if type_of_game == 1 or type_of_game == 2:
                if type_of_game == 1:
                    self.player1.choose_gesture()
                    self.player2 = Human().choose_gesture()
                    game_type = True
                elif type_of_game == 2:
                    self.player2 = AI().choose_gesture()
            elif type_of_game != 1 or type_of_game != 2:
                print('Invalid Entry.')
                type_of_game = int(input(
                    'Choose the type of game. Press "1" for Multiplayer game or Press "2" for Single Player vs. AI: '))

    def display_winner(self):
        pass

    def tbd(self):
        pass
