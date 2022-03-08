
from ai import Ai
from player import Player
from human import Human

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        



    def run_game(self):
        self.display_welcome()    # choose number of players
        self.display_gesture_options()        
        self.play_ground() 
                   # single player is you vs the ai and multiplayer is you vs another player.
        
        

    def display_gesture_options(self):
        index = 0
        for selection in self.player1.list_of_gestures or self.player2.list_of_gestures:
             print(
                 f'Press {index} for {selection}')
             index += 1
        


            
        
    def player_turn(self):
        self.display_gesture_options
        self.player1.chosen_gesture      

                # tie
                 # rules of the game
    def select_multiplayer(self):
        pass

    def select_auto_play(self):
        pass
    
       
    def display_welcome(self):
        print("Get ready to play Rock, Paper, Scissors, Lizard, Spock This is a different take of the classic rock, paper, scissors")
        print("The rules are simple:\nScissors cut Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitate Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")

    def battle(self):
        while True:
            if self.player1.score < 2 and self.player2.score < 2:   
                self.play_ground()
            else:    
                self.display_winner
            
               
    def play_ground(self):
        
        self.player1.pick_a_gesture()
        self.player2.pick_a_gesture() 
         
        if  self.player1.chosen_gesture == self.player2.chosen_gesture:
                print('You selected the same gesture. Tied')
        elif  self.player1.chosen_gesture == "rock" and self.player2.chosen_gesture == "scissor":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "scissor" and self.player2.chosen_gesture == "paper":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "paper" and self.player2.chosen_gesture == "rock":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "lizard" and self.player2.chosen_gesture == "spock":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "spock" and self.player2.chosen_gesture == "rock":
                print("Player 1 wins round")
                self.player1.score += 1
        elif  self.player1.chosen_gesture == "rock" and self.player2.chosen_gesture == "lizard":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "scissor" and self.player2.chosen_gesture == "lizard":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "paper" and self.player2.chosen_gesture == "spock":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "lizard" and self.player2.chosen_gesture == "paper":
                print("Player 1 wins round")
                self.player1.score += 1
        elif self.player1.chosen_gesture == "spock" and self.player2.chosen_gesture == "scissor":
                print("Player 1 wins round")
                self.player1.score += 1
        else:
            print("Player 2 wins round")
            self.player2.score +=1
            
        another_round = input('would you like to go again:  ')
        if another_round.upper == 'y':     
            self.battle() 
                 
            

    def display_winner(self):
        # battle ends and winner declared when one side reaeches 3
        if self.player1.score == 2:
            print('Player 1 win!!!!!')
        elif self.player2.score == 2:
            print('Player 2 win!!!!!!!!!')

    # def play_ground(self):
    #     self.player1.pick_a_gesture()
    #     self.player2.pick_a_gesture() 
    #     while True:   
    #         if  self.player1.chosen_gesture == self.player2.chosen_gesture:
    #                 print('You selected the same gesture. Tied')
    #         elif  self.player1.chosen_gesture == "rock": 
    #                 if self.player2.chosen_gesture == "scissors":
    #                     print('rock over scissors')
    #                     self.player1.score += 1
    #                 else:
    #                     print("paper over rock")
    #                     if self.player2.chosen_gesture == 'paper'
    #                     self.player2.score += 1
    #         elif self.player1.chosen_gesture == 'scissor':
    #                 if self.player2.chosen_gesture == 'paper':
    #                     print('scissor cuts paper')
    #                 else:
    #                     print('')
            # elif self.player1.chosen_gesture == "scissor" and self.player2.chosen_gesture == "paper" or "lizard":
            #         print("Player 1 wins round")
            #         self.player1.score += 1
            # elif self.player1.chosen_gesture == "paper" and self.player2.chosen_gesture == "rock" or "spock":
            #         print("Play # def playground(self):
    #     if(Scissors > Paper Paper > Rock, Rock > Lizard, Lizard > Spock, Spock > Scissors, Scissors > Lizard, Lizard > Paper, Paper > Spock, Spock > Rock, Rock > Scissors):
            
 # def dino_turn(self):
    #     self.display_gesture_options()
    #     dino_choice = int(input('Which dinosaur will attack?'))
    #     print("")
    #     self.show_robot_opponent_options()
    #     robot_choice = int(input('Which robot will defend?'))
    #     print("")
    #     self.herd.dinosaurs[dino_choice].attack(
    #         self.fleet.robots[robot_choice])
    #     if self.fleet.robots[robot_choice].health <= 0:
    #         print(f"{self.fleet.robots[robot_choice].name} has died!")
    #         self.fleet.robots.remove(self.fleet.robots[robot_choice])
#   er 1 wins round")
            #         self.player1.score += 1
            # elif self.player1.chosen_gesture == "lizard" and self.player2.chosen_gesture == "spock" or "paper":
            #         print("Player 1 wins round")
            #         self.player1.score += 1
            # elif self.player1.chosen_gesture == "spock" and self.player2.chosen_gesture == "rock" or "scissor":
            #         print("Player 1 wins round")
            #         self.player1.score += 1
    # def play_ground(self):   
    #     while True:

    #         if  self.player1.chosen_gesture == self.player2.chosen_gesture:                    
    #             print('You selected the same gesture. Tied')
    #         elif  self.player1.chosen_gesture == "rock" and self.player2.chosen_gesture == "scissor" or "lizard":
    #                 print("Player 1 wins round")
    #         elif self.player1.chosen_gesture == "scissor" and self.player2.chosen_gesture == "paper" or "lizard":
    #                 print("Player 1 wins round")
    #         elif self.player1.chosen_gesture == "paper" and self.player2.chosen_gesture == "rock" or "spock":
    #                 print("Player 1 wins round")
    #         elif self.player1.chosen_gesture == "lizard" and self.player2.chosen_gesture == "spock" or "paper":
    #                 print("Player 1 wins round")
    #         elif self.player1.chosen_gesture == "spock" and self.player2.chosen_gesture == "rock" or "scissor":
    #                 print("Player 1 wins round")
    #         else:
    #                 print("Player 2 wins")

            # else:
            #         print("Player 2 wins round")
            #         self.player2.score +=1