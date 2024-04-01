from seasons import seasons
import pytest

def main():
    test_seasons()

def test_seasons():
    assert seasons("2023-02-19") == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons("2022-02-19") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit) as err:
        seasons('cat')

if __name__ == "__main__":
    main()
