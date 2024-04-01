from plates import is_valid

def test_max_chars():
    assert is_valid("CS50") == True
    assert is_valid("CS500000") == False
    assert is_valid("CS") == True

def test_numbers():
    assert is_valid("50000") == False
    assert is_valid("CSS50") == True
    assert is_valid("CS500S") == False
    assert is_valid("CS3.133") == False
    assert is_valid("CS0133") == False

def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS,.,00") == False
