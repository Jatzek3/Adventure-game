import creature
import random
import npc

class Locations():

    def __init__(self, name):
        """Initializes a location, some location will have creature encounters,
        some will have NPC encounters."""
        self.name = name
        self.enemies = []
        self.npc = []

    def enter_location(self, hero):
        """Whenever You enter a location there will be test for hunger,
        If your food is less or equal 0 you will die"""
        hero.food -= 1
        if hero.food <= 0:
            print("""You died""")
            quit()
        return hero.food

    def fight_enemies(self, hero):
        """While there are enemies on this location you will have to fight them all"""
        while self.enemies != []:
            hero.fight(self.enemies[0])
            if self.enemies[0].hitpoints <= 0:
                dropped = random.randint(0,2)
                hero.money += dropped
                print(f"Monster dropped {dropped} money")
                self.enemies.remove(self.enemies[0])
        return self.enemies, hero.hitpoints, hero.money

    def interact_NPC(self, hero):
        if self.npc != []:
            self.npc[0].interact(hero)


class Start(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("""The sun is shining, the weather is nice""")
        super().enter_location(hero)
        rest_choice = input("Do you want to rest? Yes or no >>>")
        while rest_choice:
            hero.hitpoints += 2
            hero.food -= 1
            print("You rest for some time")
            rest_longer = input("Do you want to rest longer? Yes or no >>>")
            if rest_longer.upper()  != "YES":
                break

class Lake(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        super().enter_location(hero)
        print("You went for a stroll beside the lakeshore.")
        if hero.fishing_rod:
            print("Now that you have fishing rod do you want to catch some fish?")
            choice = input("yes or no >>>")
            if choice.upper() == "YES" or "":
                while True:
                    hero.food -= 1
                    hero.food += random.randint(0,4)
                    print("You spent some time catching fish")
                    choice = input("do you want to continue? Yes or no")
                    if choice.upper() == "YES" or "":
                        pass
                    else:
                        break


class Dungeon(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("""
        You come across dungeon entrance. You open the the gates and wild beast attack you
        from suprise
        """)
        super().enter_location(hero)
        for i in range(random.randrange(4)):
            (self.enemies.append(creature.Creature()))


class Shop(Locations):
    pass


class Forest(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("""
        You enter a forest. You know that it is quite peacefull.
        But lately when you traveled to the forest you seem to notice an
        increased number of goblins in here. Forest is good hunting grounds
        but could also have an encounter with some type of monster if you
        wont be carefull.
        """)
        super().enter_location(hero)
        for i in range(random.randrange(2)):
            (self.enemies.append(creature.Creature()))



"""Creating the world"""
start = Start("0 - Start")
lake = Lake("1 - Lake")
dungeon = Dungeon("2 - Dungeon")
shop = Shop("3 - Shop")
forest = Forest("4 - Forest")
Map = [start, lake, dungeon, shop, forest]

sigfried = npc.Shopkeeper()
shop.npc.append(sigfried)
