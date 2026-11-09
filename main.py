from entities import hero
from entities.equipment import Armor, Weapon, Collectible


if __name__ == "__main__":
    some_knight = hero.Knight("Dick")
    print(some_knight)
    sword = Weapon("меч")
    chainmail = Armor("кольчуга")
    key = Collectible("ключ")
    apple = Collectible("яблоко")
    spear = Weapon("копьё")
    some_knight.put_in_backpack(key)
    some_knight.put_in_backpack(apple)
    some_knight.put_in_backpack(chainmail)
    some_knight.put_in_backpack(sword)
    some_knight.open_backpack()
    some_knight.get_from_backpack(sword)
    some_knight.get_from_backpack(spear)
    some_knight.open_backpack()