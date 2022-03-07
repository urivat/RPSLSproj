

from ai import Ai
from human import Human


class Game:
    def __init__(self): 
        self.human = Human()
        self.ai = Ai()
    def run_game(self):
        self.display_greeting
        self.game_zone
        

    
    def game_zone():
        pass
    
    
    def player_turn(self):
        pass
    

    def display_greeting(self):
        pass
    
    def display_rule(self):
        pass
    
    def pick_player_amount():
        pass

    def display_gesture_options(self, ai):
        pass

    def show_player_options(self, gestures):
        print('Choose your gesture')
        index = 0
        for gesture in self.gestures:
            print(
                f'Press {index} for {}')
            index += 1