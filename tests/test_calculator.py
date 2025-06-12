from my_app.calculator import add
from my_app.calculator import subtract
from my_app.calculator import multiply

def test_add():
    assert add(1, 2) == 3
    def test_add():
        assert add(1, 2) == 3

    def test_subtract():
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
        assert subtract(0, 0) == 0

    def test_multiply():
        assert multiply(2, 3) == 6
        assert multiply(-1, 5) == -5
        assert multiply(0, 10) == 0
        assert multiply(2.5, 4) == 10.0
