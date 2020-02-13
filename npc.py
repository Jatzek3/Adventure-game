class NPC:

    def __init__(self):
        self.name = ""
        self.hitpoints = 100
        self.damage = 5


class Shopkeeper(NPC):

    def interact(self, hero):
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)

        self.buy = input("<")

        if self.buy == "1" and hero.money >= 10:
            hero.fishing_rod = True,
            print("You just bought a fishing rod")
            print(f"{hero.fishing_rod}")
            hero.money -= 10
        elif self.buy == "4" and hero.money >= 100:
            hero.axe = True,
            hero.money -= 50
        elif self.buy == "5" and hero.money >= 2:
            hero.food += 5
            hero.money -= 2
        else:
            print("I dont understand")


