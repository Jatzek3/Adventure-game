import locations
import creature

class Hero():

    def __init__(self, name, hitpoints, damagae):
        """Hero initializer"""
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damagae
        self.food = 100

    def go_to(self):
        """Method for choosing direction"""
        print("Where do you want to go? Enter a number")
        for i in locations.Map:
            print(i.name)
        choice = int(input())
        locations.Map[choice].enter_location(self)

    def fight(self, creature):
        """Logic behind fighting"""
        while self.hitpoints > 0 or creature.hitpoints > 0:
            print(f"You hit the creature for {self.damage} and it hit you for{creature.damage}")
            self.hitpoints = self.hitpoints - creature.damage
            creature.hitpoints = creature.hitpoints - self.damage
            print(f" You have {self.hitpoints} hitpoints left")
            print(f"Creature have {creature.hitpoints} hitpoints left")
            if self.hitpoints <= 0:
                print("You died")
                quit()
            elif creature.hitpoints <= 0:
                print("You have killed the beast")
                break
            else:
                pass




    def __str__(self):
        return ("Name: "+ str(self.name)+
                "\nHitpoints: "+ str(self.hitpoints)
                +"\nStrength: " + str(self.damage)
                +"\nFood:" + str(self.food))

    @staticmethod
    def hero_creator():
        name = input("Enter hero's name>>> ")
        hero = Hero(name, 100, 10)
        return hero


hero = Hero("Jacek", 100, 10)
hero.go_to()


