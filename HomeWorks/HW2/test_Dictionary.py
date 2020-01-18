import pytest


def test_1():
    assert 1 == 1


def test_2():
    assert 1 == 1


def test_3():
    assert 1 == 1


def test_4():
    assert 1 == 1


@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_5():
    assert 1 == 1