from random import random
from sys import exit

name = input("Hello what is your name?")



class Hero(object):
    def __init__(self, hit_points, strength, money, name, food):
            self.hit_points = hit_points
            self.strength = strength
            self.money = money
            self.name = name
            self.food = food







class NPC(object):
    def __init__(self, hit_points, strength, money):
            self.hit_points = hit_points
            self.strength = strength
            self.money = money

    Sigfrid = NPC(0, 0, 0)
    alive = True

    def shop_greating(self):
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        2.Bow                 - 20 gp
        2 Pickaxe             - 50 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)

    def buy(self):
        self.buy = input("<")

        if self.buy == "1" and Hero.money > 10:
            Hero.fishingrod = True,
            Hero.money -= 10
        elif self.buy == "2" and Hero.money > 20:
            Hero.bow = True,
            Hero.money -= 20
        elif self.buy == "3" and Hero.money > 50:
            Hero.pickaxe = True,
            Hero.money -= 50
        elif self.buy == "4" and Hero.money > 100:
            Hero.axe = True,
            Hero.money -= 100
        elif self.buy == "5" and Hero.money > 2:
            Hero.food += 5
            Hero.money -= 2
        elif  self.buy == "steal":
            pass
        elif self.buy == "attack" or "kill":
            pass
        elif self.buy == "run" or "leave":
            pass
        else:
            print("I dont understand")



class Map(object):
    """Map gonna look like this        5
                                       4
                                   3   1   2
    """

    map = {
        0: "Death",
        1: "Start",
        2: "Shop",
        3: "Lake",
        4: "Forest",
        5: "Dungeon"
    }

    exits = {
        0: {"D": 0},
        1: {"E": 2, "N": 4, "W": 3, "D": 0},
        2: {"W": 1, "D": 0},
        3: {"E": 1, "D": 0},
        4: {"S": 1, "N": 5, "D": 0},
        5: {"S": 4, "D": 0}

    }

    vocabulary = {
        "Death": "D",
        "North": "N",
        "South": "S",
        "East": "E",
        "West": "W"
    }

    loc = 1
    while True:
        availableExits = ""
        for direction in exits[loc].keys():
            availableExits += direction + ","

        print(map[loc])
        if loc == 0:
            break

        direction = input("Available exits are " + availableExits).upper()
        print()

        if len(direction) > 1:
            for word in vocabulary:
                if word in direction:
                    direction = vocabulary[word]

        if direction in exits[loc]:
            loc = exits[loc][direction]
        else:
            print("You cannot go in that direction")


class Engine(object):
    pass