from um import count

def main():
    test_um()

def test_um():
    assert count("Hello um There") == 1
    assert count("UM....") == 1
    assert count("um?") == 1
    assert count("Um, Thanks, Um....") == 2
    assert count("um") == 1
    assert count("Hello Mom hmmm ummmm Thanks for the instrument") == 0

if __name__ == "__main__":
    main()
