import pytest


def test_1(set_fixture_1):
    ln = len(set_fixture_1)
    set_fixture_1.add("red")
    assert len(set_fixture_1) == ln


def test_2(set_fixture_1, set_fixture_2):
    assert set_fixture_1.issubset(set_fixture_2)


def test_3(set_fixture_1, set_fixture_2):
    set_fixture_2.discard("black")
    set_fixture_2.discard("white")
    assert set_fixture_1 == set_fixture_2


def test_4(set_fixture_1):
    assert "white" not in set_fixture_1


@pytest.mark.parametrize("test_input", [{1, 2, 3, 4, 5}, {True, False}, {"Bob", "Bill", "Nile", "Kate"}])
def test_5(test_input):
    assert len(test_input) % 2 == 0
