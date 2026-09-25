from dataclasses import dataclass

@dataclass
class Backpack:
    item_name: str
    item_amount: int


bckpck = Backpack(item_name='someshit', item_amount=12)
print(bckpck.item_name, bckpck.item_amount)
