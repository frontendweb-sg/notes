
from random import random
from user import User


class Account(User):
    logged_in_user = None
    """
    Acount class:
    It is responsible to create an account, deposit amount, transfer amount, withdraw amount.
    1. Create new account
    2. Acount detail
    3. Deposite amount
    4. Withraw amount
    5. Transfer amount
    6. Check balance
    """

    def register(self):
        user = self.create(self)
        self.customers.append(user)
        print("Account created successfully and username is: {}".format(
            self.username))

    def login(self):
        user: User = None
        while True:
            username = input("Enter username: ")
            user = next(
                user for user in self.customers if self.username == username)
            if user is not None:
                break

        while True:
            password = input("Enter password: ")
            if user.password == password:
                self.logged_in_user = user
                print("Welcome to profile: {}".format(user.name))
                break
