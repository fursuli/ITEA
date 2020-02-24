""" Создать словарь Страна:Столица.
Создать список стран. Не все страны со списка должны сходиться с названиями стран со словаря.
С помощою оператора in проверить на вхождение элемента страны в словарь,
и если такой ключ действительно существует вывести столицу. """

dictCountries = dict(
    United_Kingdom = 'London',
    Germany = 'Berlin',
    France = 'Paris',
    Japan = 'Tokyo'
)

listCountries = [
    'Japan',
    'France',
    'United_Kingdom',
    'Italy'
]

for country in listCountries:
    if country in dictCountries:
        print(dictCountries[country])