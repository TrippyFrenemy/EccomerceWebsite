import pytest
import shop.views as views


# In console: python -m pytest -s -v test_build_and_run/
def test_check_user():
    assert views.check_user() == True


def test_check_login():
    assert views.check_login() == True


def test_check_order():
    assert views.check_order() == True


def test_check_cart():
    views.check_cart()
