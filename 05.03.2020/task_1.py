"""
 Create class Person with AbcMethods (personal_info, personal_age).
 Create child classes: Entrant(last_name, birth_date, faculty),
 Student(last_name, birth_date, faculty, year_of_studying),
 Teacher(last_name, birth_date, faculty, position, experience).
 Create list of n persons, display full info from base AND make to possible
 searching persons which required for asked diapason.
 """
from abc import ABC, abstractmethod
from datetime import date
from pprint import pprint


class AbstractPerson(ABC):

    def __init__(self, name, last_name, birth_date: date):
        self._name = name
        self._last_name = last_name
        if not isinstance(birth_date, date):
           raise TypeError('birth_date must be datetime.date value')
        else:
            self._birth_date = birth_date

    @property
    def full_name(self):
        return f'{self._name.title()} {self._last_name.title()}'

    @full_name.setter
    def full_name(self, full_name):
        self._name, self._last_name = full_name.split(' ')

    @property
    def birthday(self):
        return self._birth_date

    @birthday.setter
    def birthday(self, birth_day: date):
        self._birth_date = birth_day

    @abstractmethod
    def personal_age(self):
        today = date.today()
        if today.month < self._birth_date.month:
            if today.day < self._birth_date.day:
                age = today.year - self._birth_date.year - 1
                return age
        else:
            age = today.year - self._birth_date.year
            return age

    @abstractmethod
    def personal_info(self):
        pass


class Entrant(AbstractPerson):

    def __init__(self, name, last_name, birth_date, faculty):
        super().__init__(name, last_name, birth_date)
        self._faculty = faculty

    @property
    def personal_age(self):
        return super().personal_age()

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, faculty):
        self._faculty = faculty

    @property
    def personal_info(self):
        data = {
            'full name' : self.full_name,
            'birthday' : self._birth_date.__str__(),
            'age' : self.personal_age,
            'faculty' : self._faculty
        }
        return data


class Student(Entrant):

    def __init__(self, name, last_name, birth_date: date, faculty, year_of_studying):
        super().__init__(name, last_name, birth_date, faculty)
        self._year_of_studying = year_of_studying

    @property
    def year_of_studying(self):
        return self._year_of_studying

    @year_of_studying.setter
    def year_of_studying(self, year):
        self._year_of_studying = year

    @property
    def personal_info(self):
        data = {
            'full name' : self.full_name,
            'birthday' : self._birth_date.__str__(),
            'age' : self.personal_age,
            'faculty' : self._faculty,
            'year of studying' : self._year_of_studying
        }
        return data


class Teacher(Entrant):

    def __init__(self, name, last_name, birth_date, faculty, position, experience):
        super().__init__(name, last_name, birth_date, faculty)
        self._positions = {
            position : experience
        }

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, **kwargs):
        for position, experience in kwargs:
            if position in self._positions:
                self._positions[position] += experience
            else:
                self._positions[position] = experience

    @property
    def personal_info(self):
        exp = 0
        for key in self._positions:
            exp += self._positions[key]

        data = {
            'full name' : self.full_name,
            'birthday' : self._birth_date.__str__(),
            'age' : self.personal_age,
            'faculty' : self._faculty,
            'positions' : self._positions,
            'experience at all' : exp
        }
        return data


# entrant = Entrant('Mariia', 'Strilchuk', date(1999, 11, 21), 'BI')
# pprint(entrant.personal_info)
#
# student = Student('Mariia', 'Strilchuk', date(1999, 11, 21), 'BI', 4)
# pprint(student.personal_info)

# teacher = Teacher('Lilia', 'Galata', date(1975, 3, 16), 'KSZI', '???', 11)
# pprint(teacher.personal_info)
# teacher.positions['gdsg'] = 5
# teacher.positions['gdsg'] = 3
# pprint(teacher.personal_info)
