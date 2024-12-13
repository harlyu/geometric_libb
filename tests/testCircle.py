import pytest
import circle


class TestCircle:

    def test_area_valid(self):
        r = 3

        result = circle.area(r)
        assert result == pytest.approx(28.2743, rel=1e-5)

    def test_perimeter_valid(self):
        r = 3

        result = circle.perimeter(r)
        assert result == pytest.approx(18.8496, rel=1e-5)

    def test_area_invalid_negative_radius(self):
        r = -1
        with pytest.raises(ValueError) as excinfo:
            circle.area(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_perimeter_invalid_negative_radius(self):
        r = -1

        with pytest.raises(ValueError) as excinfo:
            circle.perimeter(r)
        assert str(excinfo.value) == "Radius must be a positive number."

    def test_area_zero_radius(self):
        r = 0

        with pytest.raises(ValueError) as excinfo:
            circle.area(r)
        assert str(excinfo.value) == "Radius mustn't be a null."

    def test_perimeter_zero_radius(self):
        r = 0

        with pytest.raises(ValueError) as excinfo:
            circle.perimeter(r)
        assert str(excinfo.value) == "Radius mustn't be a null number."

    def test_circle_functions(self):
        try:
            radius = 3
            print("Area of the circle:", circle.area(radius))
            print("Perimeter of the circle:", circle.perimeter(radius))

            radius = -1
            print("Area of the circle:", circle.area(radius))

            radius = 0
            print("Perimeter of the circle:", circle.perimeter(radius))

        except ValueError as e:
            print("Error:", e)


TestCircle().test_circle_functions()
