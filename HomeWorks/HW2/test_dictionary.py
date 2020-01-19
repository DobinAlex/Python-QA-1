import pytest


def test_1(dictionary_fixture):
    assert dictionary_fixture[3] == "three"


def test_2(dictionary_fixture):
    key = 15
    assert dictionary_fixture.get(key, "no number") == "no number"


def test_3(dictionary_fixture):
    del dictionary_fixture[2]
    assert len(dictionary_fixture) == 4


def test_4(dictionary_fixture):
    numbers2 = dictionary_fixture.copy()
    assert numbers2[3] == dictionary_fixture.get(3)


@pytest.mark.parametrize("test_input", [{"R": "red", "G": "green", "B": "blue"},
                                        {1: 100, "name": "Jack", 2: 3.33, "2": True}])
def test_5(test_input, dictionary_fixture):
    len_test_input = len(test_input)
    len_dictionary_fixture = len(dictionary_fixture)
    test_input.update(dictionary_fixture)
    assert len(test_input) == len_test_input + len_dictionary_fixture
