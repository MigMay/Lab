

class Account:
    def __init__(self, name: str) -> None:
        """
        Initialize an Account object.

        :param name: The first name of the account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        depositing amount into account

        :param amount: The amount being deposited
        :return: True if deposit was successful, otherwise false
        """

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        withdrawing amount from account

        :param amount: The amount being withdrawn
        :return: True if withdraw was successful, otherwise false
        """
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        gets the balance of the account

        :return: the account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        gets the name of the account holder

        :return: the name
        """
        return self.__account_name
