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
                RPG!        
        1. Start a new game
        3. Exit
        """)
            choice = input("Go ahead 1 or 2 . Then Press Enter> ")
            if choice == "1":
                return Hero.hero_creator()
            if choice == "2":
                exit()
            else:
                pass

