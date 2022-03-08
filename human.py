


from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def pick_name(self):
        self.player_name = input('whats your name ')
        print(self.player_name)