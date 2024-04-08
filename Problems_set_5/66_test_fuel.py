from fuel_66 import *
import pytest

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("!/!")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"
