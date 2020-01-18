import pytest


tst_list = ['a', 2, '', 55, 0, 'a']
tst_list_2 = [1, 2, 3, 4, 5]
tst_list_3 = ['a', 'b', 'abc']


def test_1():
    assert tst_list.index(55) == 1


def test_2():
    assert tst_list.count('a') == 2


def test_3():
    tst_list.clear()
    assert tst_list == []


def test_4():
    assert 1 == 1


@pytest.mark.parametrize("test_input", [tst_list, tst_list_2, tst_list_3])
def test_5(test_input):
    assert 1 == 1
