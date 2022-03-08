from fleet import Fleet
from herd import Herd
import random


class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs")

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            dice_roll = random.randint(1, 10)
            if dice_roll % 2 == 0:
                self.dino_turn()
                if len(self.fleet.robots) > 0:
                    self.robo_turn()
            else:
                self.robo_turn()
                if len(self.herd.dinosaurs) > 0:
                    self.dino_turn()

    def dino_turn(self):
        self.show_dino_opponent_options()
        dino_choice = int(input('Which dinosaur will attack?'))
        print("")
        self.show_robot_opponent_options()
        robot_choice = int(input('Which robot will defend?'))
        print("")
        self.herd.dinosaurs[dino_choice].attack(
            self.fleet.robots[robot_choice])
        if self.fleet.robots[robot_choice].health <= 0:
            print(f"{self.fleet.robots[robot_choice].name} has died!")
            self.fleet.robots.remove(self.fleet.robots[robot_choice])

    def robo_turn(self):
        self.show_robot_opponent_options()
        robot_choice = int(input(f"Which robot will attack?"))
        print("")
        self.show_dino_opponent_options()
        dino_choice = int(input(f"Which dinosaur will defend?\n"))

        self.fleet.robots[robot_choice].attack(
            self.herd.dinosaurs[dino_choice])

        if self.herd.dinosaurs[dino_choice].health <= 0:
            print(f"{self.herd.dinosaurs[dino_choice].name} has died!")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_choice])

    def show_dino_opponent_options(self):
        print('Choose your dinosaur!')
        index = 0
        for dinosaur in self.herd.dinosaurs:
            print(
                f'Press {index} for {dinosaur.name} with {dinosaur.health} health')
            index += 1

    def show_robot_opponent_options(self):
        print('Choose your robot!')
        index = 0
        for robot in self.fleet.robots:
            print(f"Press {index} for {robot.name} with {robot.health} health")
            index += 1

    def display_winners(self):
        # battle ends and winner declared when HP is zero for all of one side
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
            print('Robots win!!!!!')
        else:
            print('Dinosaurs win!!!!!!!!!')
