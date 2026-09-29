import heroes


if __name__ == '__main__':
    some_knight = heroes.Knight('Dick')
    print(some_knight)
    some_knight.put_in_backpack('key')
    some_knight.put_in_backpack('apple', 12) # todo давай возьмем за правило передавать все именованные аргументы
    # поднимем читабельность + избавим себя от возможной ошибки
    some_knight.put_in_backpack('key')
    some_knight.open_backpack()
    some_knight.get_from_backpack('key', 5)
    some_knight.open_backpack()
    some_knight.get_from_backpack('apple', 5)
