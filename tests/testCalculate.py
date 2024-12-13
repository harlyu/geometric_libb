import pytest
from calculate import calc
import math


class TestCalculateFunctions:

    def test_calc_circle_area(self):
        radius = [5]

        result = calc('circle', 'area', radius)

        assert result == pytest.approx(78.53981633974483)

    def test_calc_square_area(self):
        side_length = [4]

        result = calc('square', 'area', side_length)

        assert result == 16

    def test_calc_triangle_area(self):
        a, b, c = 3, 4, 5
        p = (a + b + c) / 2
        expected_area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

        result = calc('triangle', 'area', [3, 4, 5])

        assert result == pytest.approx(expected_area)

    def test_calc_triangle_perimeter(self):
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c

        result = calc('triangle', 'perimeter', [3, 4, 5])

        assert result == expected_perimeter

    def test_calc_invalid_figure(self):
        with pytest.raises(AssertionError):
            calc('ellipse', 'area', [5])

    def test_calc_invalid_function(self):
        with pytest.raises(AssertionError):
            calc('circle', 'height', [5])

    def test_calc_triangle_invalid_sides(self):
        with pytest.raises(ValueError):
            calc('triangle', 'area', [1, 2, 3])
