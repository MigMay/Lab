import pytest
from account import *

class Test:
    def setup_method(self):
        self.account = Account('bob')

    def teardown_method(self):
        del self.account

    def test_deposit(self):
        success = self.account.deposit(15.10)
        assert success
        success = self.account.deposit(-5.25)
        assert not success

    def test_withdraw(self):
        self.account.deposit(20)
        success = self.account.withdraw(15.10)
        assert success
        success = self.account.withdraw(25.25)
        assert not success
        success = self.account.withdraw(-5.25)
        assert not success

    def test_get_balance(self):
        balance = self.account.get_balance()
        assert balance == 0

        self.account.deposit(20)
        balance = self.account.get_balance()
        assert balance == 20

        self.account.withdraw(21)
        balance = self.account.get_balance()
        assert balance == 20

        self.account.withdraw(5.25)
        balance = self.account.get_balance()
        assert balance == pytest.approx(14.75, 0.01)


    def test_get_name(self):
        name = self.account.get_name()
        assert name == 'bob'
