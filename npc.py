class NPC:

    def __init__(self):
        self.name = ""
        self.hitpoints = 100
        self.damage = 5


    def interact(self, hero):
        pass


class Shopkeeper(NPC):
    pass
    # def shop_greating(self):
    #     print("""
    #     Greeting traveller. What do you wish to have?
    #     1.FishingRod          - 10 gp
    #     2.Bow                 - 20 gp
    #     2 Pickaxe             - 50 gp
    #     4.Axe                 - 100 gp
    #     5. or maybe some food?-  2 gp
    #     """)
    #
    # def buy(self):
    #     self.buy = input("<")
    #
    #     if self.buy == "1" and Hero.money > 10:
    #         Hero.fishingrod = True,
    #         Hero.money -= 10
    #     elif self.buy == "2" and Hero.money > 20:
    #         Hero.bow = True,
    #         Hero.money -= 20
    #     elif self.buy == "3" and Hero.money > 50:
    #         Hero.pickaxe = True,
    #         Hero.money -= 50
    #     elif self.buy == "4" and Hero.money > 100:
    #         Hero.axe = True,
    #         Hero.money -= 100
    #     elif self.buy == "5" and Hero.money > 2:
    #         Hero.food += 5
    #         Hero.money -= 2
    #     elif  self.buy == "steal":
    #         pass
    #     elif self.buy == "attack" or "kill":
    #         pass
    #     elif self.buy == "run" or "leave":
    #         pass
    #     else:
    #         print("I dont understand")
    #
