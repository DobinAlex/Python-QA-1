import pytest


@pytest.fixture
def dictionary_fixture():
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    return numbers


@pytest.fixture
def set_fixture_1():
    colors = {"red", "green", "blue"}
    return colors


@pytest.fixture
def set_fixture_2():
    colors = {"red", "green", "blue", "black", "white"}
    return colors
