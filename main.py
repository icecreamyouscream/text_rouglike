import heroes
from equipment import Armor, Weapon, Collectible


if __name__ == "__main__":
    some_knight = heroes.Knight("Dick")
    print(some_knight)
    sword = Weapon("меч")
    chainmail = Armor("кольчуга")
    key = Collectible("ключ")
    apple = Collectible("яблоко")
    some_knight.put_in_backpack(key)
    some_knight.put_in_backpack(apple)
    some_knight.put_in_backpack(chainmail)
    some_knight.put_in_backpack(sword)
    some_knight.put_in_backpack(sword)
    some_knight.open_backpack()
    some_knight.get_from_backpack(sword)
    some_knight.get_from_backpack("сад")
    some_knight.open_backpack()