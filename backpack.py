from dataclasses import dataclass


@dataclass
class Backpack:
    storage: dict

    def add_stuff(self, dct):
        for key, value in dct.items():
            if key not in self.storage:
                self.storage.update(dct)
            else:
                self.storage[key] += value

    def show_storage(self):
        print('Items in backpack:')
        print(*{f'\n    {key}: {value}' for key, value in self.storage.items()})
