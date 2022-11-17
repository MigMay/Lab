import pytest
from account import *


@pytest.fixture
def account():
    return Account('bob')


def test_deposit(account):
    success = account.deposit(15.10)
    assert success
    success = account.deposit(-5.25)
    assert not success


def test_withdraw(account):
    account.deposit(20)
    success = account.withdraw(15.10)
    assert success
    success = account.withdraw(25.25)
    assert not success
    success = account.withdraw(-5.25)
    assert not success


def test_get_balance(account):
    balance = account.get_balance()
    assert balance == 0

    account.deposit(20)
    balance = account.get_balance()
    assert balance == 20

    account.withdraw(21)
    balance = account.get_balance()
    assert balance == 20

    account.withdraw(5.25)
    balance = account.get_balance()
    assert balance == pytest.approx(14.75, 0.01)


def test_get_name(account):
    name = account.get_name()
    assert name == 'bob'
