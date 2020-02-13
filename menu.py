import time
from hero import Hero


class Menu:

    def welcome_screen(self):
        print("""        ____________________________
        Welcome to my Text based RPG
        Loading. Please wait.
         """)
        time.sleep(1)

    def menu_screen(self):
        while True:
            print("""
        Greeting to my very simple RPG game the main goal of the game is to survive.
        On the starting location you can rest giving you 2 hp but take 1 food
        On Lake you can catch a fish for food if you have a rod
        In the the Dungeon you can encounter monster witch will drop money
        In the shop you can buy fishing rod, food or an axe
        Have fuN!
                
        1. Start a new game
        2. Exit
        """)
            choice = input("Go ahead 1 or 2 . Then Press Enter> ")
            if choice == "1":
                return Hero.hero_creator()
            if choice == "2":
                exit()
            else:
                pass

