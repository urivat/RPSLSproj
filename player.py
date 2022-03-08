class Player:
    def __init__(self):
        self.list_of_gestures = ['rock','paper','scissor','lizard','spoke']
       
    
    
    def pick_a_gesture(self, user_picks):
        user_picks = input('Pick a choice: (rock,\n paper,\n scissor,\n lizard,\n spoke\n')
        return user_picks