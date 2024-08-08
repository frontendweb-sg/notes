from datetime import datetime
from account import Account
from user import User


class Bank(Account, User):
    """
    Bank class
    """
    customers = []
    bank_name = "SBI"
    total_deposit: float = 0.0
    establish_date = datetime(1992, 1, 10)

    def __init__(self) -> None:
        super().__init__()
        pass

    def withdraw(self, amt: float):
        pass

    def deposit(self, amt: float):
        pass

    def balance(self):
        if self.logged_in_user is not None:
            return self.logged_in_user.balance

    @classmethod
    def init(cls):
        msg = """
        Acount class:
        It is responsible to create an account, deposit amount, transfer amount, withdraw amount.
        1. Create new account
        2. Login Account
        3. Deposite amount
        4. Withraw amount
        5. Transfer amount
        6. Check balance
        """
        print(msg)
        while True:
            option = int(input())
            if option == 1:
                cls.register(cls)
            elif option == 2:
                cls.login(cls)
            elif option == 3:
                cls.balance(cls)
            else:
                break
