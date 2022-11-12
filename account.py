class Account:
    def __init__(self, name: str | None) -> None:
        """
        Initialize an Account object.

        :param name: The first name of the account.
        """
        self.__account_name: str | None = name
        self.__account_balance: float = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 or amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
