""" 1 """

class Auto:

    _number = None
    _color = None
    _chassis_type = "wheeled"
    _fuel = 'petrol'

    def __init__(self, color, mileage=0):
        self._color = color
        self._mileage = mileage

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    def get_color(self):
        return self._color

    def recolor(self, new_color):
        self._color = new_color
        print(f"Auto was recolored to {self._color}.")

    def get_chss_type(self):
        return self._chassis_type

    def get_mileage(self):
        return self._mileage

    def mileage_increase(self, distanse):
        self._mileage += distanse
        print(f'Mileage of this auto = {self._mileage}')



class Car(Auto):

    _capacity = 4

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, new_capacity):
        self._capacity = new_capacity

    def recolor(self, new_color):

        choice = input(f'Do You want to change {self._color} to {new_color} color? [y/n] ')

        if choice == 'y' or choice == 'yes':
            self._color = new_color
            print(f'Car was colored to {self._color}')
        elif choice == 'n' or choice == 'no':
            print('Recoloring denied.')
        else:
            print("It's not an answer, I'll do nothing.")


    def mileage_increase(self, distanse):
        self._mileage += distanse
        print(f'Mileage of this Car = {self._mileage}')


class Truck(Auto):

    cargo_type = None
    carrying_capacity = 10

    def mileage_increase(self, distanse):
        self._mileage += distanse
        print(f'Mileage of this Truck = {self._mileage}')

    def change_carr_capacity(self, new_capacity):
        self.carrying_capacity = new_capacity
        print(f'Carrying capacity of this Truck for now : {self.carrying_capacity}')


""" Ch """
auto = Auto('AF2347')
car1 = Car('black', 5000)
car2 = Car('red', 10000)
truck1 = Truck('blue')
truck2 = Truck('black', 7000)

car1.recolor('red')
print(car1.get_mileage())
car1.mileage_increase(400)
print(car1.get_mileage())
truck1.recolor('white')

print(car1.get_number())
car1.set_number('VB32543')
print(car1.get_number())
