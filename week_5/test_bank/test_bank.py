from bank import value

def test_bank_normal():
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("How ya doing") == 20
    assert value("Hello, You") == 0

def test_bank_capital():
    assert value("hElLo, YoOu") == 0
    assert value("HIIIII") == 20
