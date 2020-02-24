""" Создать список из N элементов (от 0 до n с шагом 1).
В этом списке вывести все четные значения. """
try:
    user_input = int(input("Enter n of elements, please: "))
except ValueError:
    print('Invalid input')
for number in range(0, user_input):
    if number % 2 == 0:
        print(number)