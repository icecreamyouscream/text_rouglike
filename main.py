import heroes


if __name__ == '__main__':
    some_knight = heroes.Knight('Dick')
    print(some_knight)
    some_knight.put_in_backpack('key')
    some_knight.put_in_backpack('apple', 12)
    some_knight.put_in_backpack('leather', 5)
    some_knight.put_in_backpack('key')
    some_knight.open_backpack()
