""" 2 """
class Shop:

    solded_at_all = 0

    def __init__(self, shop_name, solded_enum:int):
        self._shop_name = shop_name
        self._solded_enum = solded_enum
        #  Додавання к-сті проданих товарів до загальної кількості одразу при створенні об'єкту
        Shop.solded_at_all += self._solded_enum


    def increase_all_sales(self, solded_enum):
        self._solded_enum += solded_enum
        Shop.solded_at_all += solded_enum

    def solded(self):
        print(f'At all : {Shop.solded_at_all}')


shop1 = Shop('ASD', 400)
shop2 = Shop('ZXC', 653)
shop3 = Shop('JOJO', 100)
shop4 = Shop('glhf', 5000)
shop5 = Shop('ggwp', 200)

print(Shop.solded_at_all)

shop1.increase_all_sales(47)
print(Shop.solded_at_all)
