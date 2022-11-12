


class Account:


    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    def get_name(self):
        pass

