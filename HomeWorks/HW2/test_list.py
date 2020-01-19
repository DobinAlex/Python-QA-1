import pytest


tst_list = ['a', 2, '', 55, 0, 'a']
tst_list_2 = [1, 2, 3, 4, 5]
tst_list_3 = ['a', 'b', 'abc']


def test_1():
    assert tst_list.index(55) == 3


def test_2():
    assert tst_list.count('a') == 2


def test_3():
    assert type(tst_list[5]) == str


def test_4():
    tst_list.clear()
    assert tst_list == []


@pytest.mark.parametrize("test_input", [tst_list, tst_list_2, tst_list_3])
def test_5(test_input):
    test_input.append(33)
    test_input.reverse()
    print(test_input)
    assert test_input.index(33) == len(test_input)-1

