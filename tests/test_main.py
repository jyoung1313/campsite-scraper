from scraper.main import add, subtract


def test_add():
    assert add(1, 4) == 5

def test_subtract():
    assert subtract(4, 2) == 2