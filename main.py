from hero import Hero
from menu import Menu
import locations
from locations import Start, Lake, Dungeon, Shop, Forest


if __name__ == "__main__":


    """Creating a hero"""
    menu_object = Menu()
    menu_object.welcome_screen()
    hero = menu_object.menu_screen()
    while True:
        hero.go_to()
        hero.present_location.enter_location(hero)
        hero.present_location.fight_enemies(hero)
        hero.present_location.interact_NPC(hero)
        print(hero)