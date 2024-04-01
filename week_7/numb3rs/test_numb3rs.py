from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("2.400.21.1") == False
    assert validate
    assert validate("200.1.1.1") == True
    assert validate("cat.1.2.2") == False
    assert validate("1") == False
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("Hello") == False
    assert validate("1.1.1.") == False
    assert validate("1.2.3.1000") == False

if __name__ == "__main__":
    main()
