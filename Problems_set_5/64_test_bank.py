from bank_64 import value


def test_value():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0

    assert value("h") == 20
    assert value("H") == 20

    assert value("flip world") == 100
    assert value("FLIP WORLD") == 100
