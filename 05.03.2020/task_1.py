"""
 Create class Person with AbcMethods (personal_info, personal_age).
 Create child classes: Entrant(last_name, birth_date, faculty),
 Student(last_name, birth_date, faculty, year_of_studying),
 Teacher(last_name, birth_date, faculty, position, experience).

 Create list of n persons, display full info from base AND make to possible
 searching persons which required for asked diapason.
 """
from abc import ABC, abstractmethod


class AbstractPerson(ABC):

    @abstractmethod
    def personal_info(self):
        pass

    @abstractmethod
    def birth_date(self):
        pass

    @abstractmethod
    def personal_age(self):
        pass

