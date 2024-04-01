from twttr import shorten

def test_twttr_normal():
    assert shorten("Hello") == "Hll"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_twttr_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("WHAT's YOUR NAME?") == "WHT's YR NM?"

def test_twttr_nums():
    assert shorten("1234456") == "1234456"
