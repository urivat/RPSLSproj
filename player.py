

class Player:
    def __init__(self, name):
        self.gesture = ['rock', 'paper' ,'scissors', 'lizard', 'spock']
        self.name = name
        

    def pick_a_gesture(self, ):
        print('Choose your gesture!')
        index = 0
        for gesture in self.gesture :
            print(
                f'Press {index} for {gesture.name}')
            index += 1


        
        

