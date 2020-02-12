class NPC:

    def __init__(self):
        self.name = ""
        self.hitpoints = 100
        self.damage = 5


class Shopkeeper(NPC):

    def interact(self, buyer):
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)

        self.buy = input("<")

        if self.buy == "1" and buyer.money >= 10:
            buyer.fishing_rod = True,
            buyer.money -= 10
        elif self.buy == "4" and buyer.money >= 100:
            buyer.axe = True,
            buyer.money -= 50
        elif self.buy == "5" and buyer.money >= 2:
            buyer.food += 5
            buyer.money -= 2
        else:
            print("I dont understand")


