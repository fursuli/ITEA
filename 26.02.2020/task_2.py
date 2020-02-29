""" 2 """
class Shop:

    solded_at_all = 0

    def __init__(self, shop_name, solded_enum:int):
        self.shop_name = shop_name
        self.solded_enum = solded_enum
        Shop.solded_at_all += self.solded_enum

    def solded(self):
        print(f'At all : {Shop.solded_at_all}')


shop1 = Shop('ASD', 400)
shop2 = Shop('ZXC', 653)
shop3 = Shop('JOJO', 100)


print(Shop.solded_at_all)
