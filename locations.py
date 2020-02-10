

class Locations():

    def __init__(self, name):
        self.name = name
        self.enemies = []
        self.npc = []


    def enter_location(self, hero):
        hero.food -= 1
        if self.enemies != []:
            for i in self.enemies:
                hero.fight(i)
        if self.npc != []:
            print("Who do you want to approach?")
            counter = 0
            for i in self.npc:
                print(counter), print(i.name)
                counter += 1
            choice = int(input())
            self.npc[choice].interact(hero)

        return hero.food


class Start(Locations):
    pass

class Lake(Locations):
    pass

class Dungeon(Locations):
    pass

class Shop(Locations):
    pass



Map =[Start("0 - Start"),
Lake("1 - Lake"),
Dungeon("2 - Dungeon"),
Shop("3 - Shop"),]