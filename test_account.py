import pytest
from account import *


class Test:
    def setup_method(self):
        self.account = Account('bob')

    def teardown_method(self):
        del self.account

    def test_init(self):
        assert self.account.get_name() == 'bob'
        assert self.account.get_balance() == 0

    def test_deposit(self):
        assert self.account.deposit(15.10) is True
        assert self.account.get_balance() == pytest.approx(15.10, abs=0.001)
        assert self.account.deposit(-5.25) is False
        assert self.account.get_balance() == pytest.approx(15.10, abs=0.001)
        assert self.account.deposit(0) is False
        assert self.account.get_balance() == pytest.approx(15.10, abs=0.001)
        assert self.account.deposit(5) is True
        assert self.account.get_balance() == pytest.approx(20.10, abs=0.001)

    def test_withdraw(self):
        self.account.deposit(20)
        assert self.account.withdraw(15.10) is True
        assert self.account.get_balance() == pytest.approx(4.90, abs=0.001)
        assert self.account.withdraw(25.25) is False
        assert self.account.get_balance() == pytest.approx(4.90, abs=0.001)
        assert self.account.withdraw(-5.25) is False
        assert self.account.get_balance() == pytest.approx(4.90, abs=0.001)
        assert self.account.withdraw(3) is True
        assert self.account.get_balance() == pytest.approx(1.90, abs=0.001)
        assert self.account.withdraw(0) is False
        assert self.account.get_balance() == pytest.approx(1.90, abs=0.001)
