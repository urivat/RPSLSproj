

from player import Player
from human import Human

class Game:
    def __init__(self):
        self.player = Player()
        self.human = Human()




    def run_game(self):
        self.display_welcome()
        self.display_gesture_options()


    def play_ground(self):
        pass # rules of the game

    def display_gesture_options(self):
        index = 0
        for selection in self.player.list_of_gestures:
            print(
                f'Press {index} for {selection}')
            index += 1

    def select_multiplayer(self):
        pass

    def select_auto_play(self):
        pass
    
    def display_welcome(self):
        print('This is a different take of the classic rock, paper, scissors' 
        ' welcome to the RPSLS.')
    