import pytest
import square
import math

class TestSquare:

    def test_area_correct(self):
        a = 4

        result = square.area(a)
        assert result == 16

    def test_perimeter_correct(self):
        a = 4

        result = square.perimeter(a)
        assert result == 16

    def test_area_invalid_negative_side(self):
        a = -1

        with pytest.raises(ValueError) as excinfo:
            square.area(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_perimeter_invalid_negative_side(self):
        a = -1

        with pytest.raises(ValueError) as excinfo:
            square.perimeter(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_area_zero_side(self):
        a = 0

        with pytest.raises(ValueError) as excinfo:
            square.area(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_perimeter_zero_side(self):
        a = 0

        with pytest.raises(ValueError) as excinfo:
            square.perimeter(a)
        assert str(excinfo.value) == "Side must be positive."

    def test_square_functions(self):
        try:
            side = 4
            print("Area of the square:", square.area(side))
            print("Perimeter of the square:", square.perimeter(side))

            side = -1
            print("Area of the square:", square.area(side))

            side = 0
            print("Perimeter of the square:", square.perimeter(side))

        except ValueError as e:
            print("Error:", e)


TestSquare().test_square_functions()
