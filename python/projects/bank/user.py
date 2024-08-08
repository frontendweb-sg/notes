from random import random


class User:
    def __init__(self) -> None:
        self.__name = None
        self.__username: str = None
        self.__email: str = None
        self.__password: str = None
        self.__account_number = None
        self.__address: str = None
        self.__balance: float = 0.0
        self.__history = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        self.__username = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value: str):
        self.__balance = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        self.__password = value

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value: str):
        self.__account_number = value

    def create(self):
        self.account_number = str(random()).rstrip(".")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        email = input("Enter email id: ")
        password = input("Enter password: ")
        self.name = fname + ' '+lname
        self.email = email
        self.password = password
        self.username = self.name.lower().replace(' ', '_')+str(random())
        return self
