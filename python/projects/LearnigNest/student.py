from school import School
import random


class Student(School):
    """Student class for generate student data to add in the school"""

    def __init__(self) -> dict:
        super().__init__()
        self.stu_id = 0
        self.__name = ''
        self.__age = ''
        self.__father_name = ''
        self.__mother_name = ''
        self.__class_name = ''
        self.__address = {}
        self.__state = ''
        self.__city = ''

    def add(self):
        self.stu_id = random.random()
        self.__name = input("Enter name: ")
        self.__age = input("Enter age: ")
        self.__father_name = input("Enter father name: ")
        self.__mother_name = input("Enter mother name: ")
        self.__class_name = input("Class to enroll: ")
        self.__state = input("State: ")
        self.__city = input
        self.__address = input("Address: ")

        # add info
        self.registration(self)
