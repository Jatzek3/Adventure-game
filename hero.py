import locations
import creature
import time


class Hero():

    def __init__(self, name, hitpoints, damage):
        """Hero initializer"""
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.food = 20
        self.present_location =""
        self.fishing_rod = False
        self.axe = False
        self.money = 5

    def go_to(self):
        """Method for choosing direction"""
        print("Where do you want to go? Enter a number ")
        for i in locations.Map:
            print(i.name)
        choice = int(input())
        self.present_location = locations.Map[choice]
        return self.present_location

    def fight(self, beast):
        """Logic behind fighting"""
        while self.hitpoints > 0 or beast.hitpoints > 0:
            print(f"You hit the creature for {self.damage} and it hit you for{beast.damage}")
            self.hitpoints = self.hitpoints - beast.damage
            beast.hitpoints = beast.hitpoints - self.damage
            time.sleep(1)
            print(f" You have {self.hitpoints} hitpoints left")
            print(f"Creature have {beast.hitpoints} hitpoints left")
            if self.hitpoints <= 0:
                print("You died")
                quit()
            elif beast.hitpoints <= 0:
                print("You have killed the beast")
                break
            else:
                pass

    def __str__(self):
        return ("Name: " + str(self.name) +
                "\nHitpoints: " + str(self.hitpoints)
                + "\nStrength: " + str(self.damage)
                + "\nFood:" + str(self.food)
                + "\nMoney"+ str(self.money))

    @staticmethod
    def hero_creator():
        name = input("Enter hero's name>>> ")
        hero = Hero(name, 20, 5)
        return hero


