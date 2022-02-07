# (10 points): As a player, I want the correct player to win a given round based on the choices* made by each player.
# (10 points): As a player, I want the game of RPSLS to be at minimum a 'best of three' to decide a winner.
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None

    def run_game(self):
        pass

    def display_welcome(self):
        # \n = space for visual
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
        print('The first player to win TWICE wins the Game.')
