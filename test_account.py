import pytest
from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('bob')

    def teardown_method(self):
        del self.account1

    def test_init(self):
        assert self.account1.get_name() == 'bob'
        assert self.account1.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(5) is True
        assert self.account1.get_balance() == 5
        assert self.account1.deposit(-5) is False
        assert self.account1.get_balance() == 5
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == 5
        assert self.account1.deposit(15.10) is True
        assert self.account1.get_balance() == pytest.approx(20.10, abs=0.001)
        assert self.account1.deposit(-5.25) is False
        assert self.account1.get_balance() == pytest.approx(20.10, abs=0.001)

    def test_withdraw(self):
        assert self.account1.withdraw(1) is False
        assert self.account1.get_balance() == 0
        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == 0
        self.account1.deposit(20)
        assert self.account1.withdraw(15.10) is True
        assert self.account1.get_balance() == pytest.approx(4.90, abs=0.001)
        assert self.account1.withdraw(-5.25) is False
        assert self.account1.get_balance() == pytest.approx(4.90, abs=0.001)
        assert self.account1.withdraw(3) is True
        assert self.account1.get_balance() == pytest.approx(1.90, abs=0.001)
