from hello import greet


def test_greet_world():
    assert greet("World") == "Hello, World!"


def test_greet_name():
    assert greet("Santhosh") == "Hello, Santhosh!"


def test_greet_empty():
    assert greet("") == "Hello, !"
