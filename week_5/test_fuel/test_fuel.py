from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    with pytest.raises(ValueError):
        assert convert("cat/dog")
        assert convert("3/2")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
