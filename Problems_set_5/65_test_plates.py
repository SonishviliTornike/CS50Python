from plates_65 import is_valid



def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False