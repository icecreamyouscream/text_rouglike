import heroes
from equipment import Equip


if __name__ == '__main__':
    some_knight = heroes.Knight('Dick')
    print(some_knight)
    sword = Equip('меч')
    key = Equip('ключ')
    apple = Equip('яблоко')
    some_knight.put_in_backpack('ключи', key)
    some_knight.put_in_backpack('еда', apple)
    some_knight.open_backpack()
    some_knight.put_in_backpack('оружие', sword)
    some_knight.put_in_backpack('оружие', sword)
    some_knight.open_backpack()
    some_knight.get_from_backpack(sword)
    some_knight.open_backpack()
