import pytest


@pytest.fixture
def string_fixture():
    tst_string = "Тестируемая строка"
    return tst_string


def test_1(string_fixture):
    assert string_fixture[0:4].upper() == "ТЕСТ"


def test_2(string_fixture):
    assert string_fixture.find("строка") == 12


def test_3(string_fixture):
    new_str = string_fixture.replace(" ", "")
    assert new_str.isalpha()


def test_4(string_fixture):
    assert string_fixture > "25000"


@pytest.mark.parametrize("test_input", ["test1", "test string 2", "Test Test Test"])
def test_5(test_input):
    assert test_input.istitle()
