import creature
import random

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
                self.enemies.remove(self.enemies[0])
        return self.enemies, hero.hitpoints

    # def interact_NPC(self,hero):
    #
    #     if self.npc != []:
    #         print("Who do you want to approach?")
    #         counter = 0
    #         for i in self.npc:
    #             print(counter), print(i.name)
    #             counter += 1
    #         choice = int(input())
    #         self.npc[choice].interact(hero)


class Start(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("""The sun is shining, the weather is nice""")
        super().enter_location(hero)


class Lake(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("You went for a stroll beside the lakeshore.")
        super().enter_location(hero)


class Dungeon(Locations):
    """Location inherits all methods from parent location + gives you description of itself"""
    def enter_location(self, hero):
        print("""
        You come across dungeon entrance. You open the the gates and wild beast attack you
        from suprise
        """)
        super().enter_location(hero)
        for i in range(random.randrange(3)):
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
        for i in range(random.randrange(1)):
            (self.enemies.append(creature.Creature()))



"""Creating the world"""
start = Start("0 - Start")
lake = Lake("1 - Lake")
dungeon = Dungeon("2 - Dungeon")
shop = Shop("3 - Shop")
forest = Forest("4 - Forest")
Map = [start, lake, dungeon, shop, forest]
