from working import convert
import pytest

def main():
    test()

def test():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:10 AM to 5:20 PM") == "09:10 to 17:20"
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:30 AM to 5:70 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 14:00")
    with pytest.raises(ValueError):
        convert("5 AM - 10AM")

if __name__ == "__main__":
    main()
