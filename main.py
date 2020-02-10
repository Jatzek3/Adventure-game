from hero import Hero
from menu import Menu
import locations
from locations import Start, Lake, Dungeon, Shop, Locations


if __name__ == "__main__":

    menu_object = Menu()
    menu_object.welcome_screen()
    hero = menu_object.menu_screen()
    print(hero)
    map = locations.Map
    hero.go_to()
