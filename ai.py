

import random
from player import Player


class Ai(Player):
    def __init__(self):
        super().__init__()

    def pick_a_gesture(self):
        auto_choices = self.list_of_gestures
        self.chosen_gesture = random.choice(auto_choices)

        

# gesture = Ai()
# gesture.pick_a_gesture()
# print(gesture)
        