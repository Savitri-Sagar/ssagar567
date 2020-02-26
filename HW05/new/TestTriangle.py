from Triangle import triangle
import unittest
class TestCases(unittest.TestCase):
    """This is a testing class for the classify_triangles method"""

    def test_equilateral_triangle(self):
        assert classify_triangle(2, 2, 2) == 'Equilateral triangle'
        assert classify_triangle(10, 10, 10) == 'Equilateral triangle'
        assert classify_triangle(3, 3, 3) != 'Equilateral triangle'

    def test_right_angled_triangle(self):
        """Test that right triangles are identified"""
        assert classify_triangle(16, 18, 9) == 'Right angled triangle'
        assert classify_triangle(18, 35, 43) == 'Right angled triangle'
        assert classify_triangle(13, 6, 14) == 'Right angled triangle'

    def test_isoceles_triangle(self):
        assert classify_triangle(15, 15, 11) != 'Isoceles triangle'
        assert classify_triangle(8, 8, 4) == 'Isoceles triangle'

    def test_Scalene_triangle(self):
        assert classify_triangle(12, 8, 13) == 'Scalene triangle'
        assert classify_triangle(8, 6, 10) == 'Scalene triangle'

    def test_invalid_triangle(self):
        assert classify_triangle(-8, 100, -0) == 'invalid input'
        assert classify_triangle(0, 0, 0) == 'invalid input'


if __name__ == '__main__':
    
    unittest.main(exit=False, verbosity=2)
