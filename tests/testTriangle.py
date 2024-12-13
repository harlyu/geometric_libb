import pytest
from triangle import area, perimeter


class TestTriangle:

    def test_area_correct(self):
        a, b, c = 9, 12, 15

        result = area(a, b, c)
        assert result == 54.0

    def test_perimeter_valid(self):
        a, b, c = 9, 12, 15

        result = perimeter(a, b, c)
        assert result == 36

    def test_area_invalid_sides(self):
        a, b, c = 1, 2, 3

        with pytest.raises(ValueError) as excinfo:
            area(a, b, c)
        assert str(excinfo.value) == "The given sides do not form a valid triangle."

    def test_perimeter_invalid_negative_side(self):
        a, b, c = -1, 2, 3

        with pytest.raises(ValueError) as excinfo:
            perimeter(a, b, c)
        assert str(excinfo.value) == "Sides must be positive numbers."

    def test_area_zero_side(self):
        a, b, c = 0, 2, 3

        with pytest.raises(ValueError) as excinfo:
            area(a, b, c)
        assert str(excinfo.value) == "Sides must be positive numbers."

    def test_perimeter_zero_side(self):
        a, b, c = 0, 2, 3

        with pytest.raises(ValueError) as excinfo:
            perimeter(a, b, c)
        assert str(excinfo.value) == "Sides must be positive numbers."

    def test_triangle_functions(self):
        try:
            side_a = 3
            side_b = 4
            side_c = 5

            print("Triangle area:", area(side_a, side_b, side_c))
            print("Triangle perimeter:", perimeter(side_a, side_b, side_c))

            side_a = 1
            side_b = 2
            side_c = 3

            print("Triangle area:", area(side_a, side_b, side_c))

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    TestTriangle().test_triangle_functions()
