
# from Triangle import triangle
# import unittest
# class TestCases(unittest.TestCase):
#     """This is a testing class for the classify_triangles method"""

#     def test_equilateral_triangle(self):
#         assert triangle(2, 2, 2) == 'Equilateral triangle'
#         assert triangle(10, 10, 10) == 'Equilateral triangle'
#         assert triangle(3, 3, 3) != 'Equilateral triangle'

#     def test_right_angled_triangle(self):
#         """Test that right triangles are identified"""
#         assert triangle(16, 18, 9) == 'Right angled triangle'
#         assert triangle(18, 35, 43) == 'Right angled triangle'
#         assert triangle(13, 6, 14) == 'Right angled triangle'

#     def test_isoceles_triangle(self):
#         assert triangle(15, 15, 11) != 'Isoceles triangle'
#         assert triangle(8, 8, 4) == 'Isoceles triangle'

#     def test_Scalene_triangle(self):
#         assert triangle(12, 8, 13) == 'Scalene triangle'
#         assert triangle(8, 6, 10) == 'Scalene triangle'

#     def test_invalid_triangle(self):
#         assert triangle(-8, 100, -0) == 'invalid input'
#         assert triangle(0, 0, 0) == 'invalid input'


# if __name__ == '__main__':
    
#     unittest.main(exit=False, verbosity=2)

from Triangle import triangle
import unittest
class TestCases(unittest.TestCase):
    """This is a testing class for the classify_triangles method"""

    def test_equilateral_triangle(self):
        assert triangle(2, 2, 2) == 'Equilateral triangle'
        assert triangle(10, 10, 10) == 'Equilateral triangle'
        assert triangle(3, 3, 3) != 'Equilateral triangle'

    def test_right_angled_triangle(self):
        """Test that right triangles are identified"""
        assert triangle(16, 18, 9) == 'Right angled triangle'
        assert triangle(18, 35, 43) == 'Right angled triangle'
        assert triangle(13, 6, 14) == 'Right angled triangle'

    def test_isoceles_triangle(self):
        assert triangle(15, 15, 11) != 'Isoceles triangle'
        assert triangle(8, 8, 4) == 'Isoceles triangle'

    def test_Scalene_triangle(self):
        assert triangle(12, 8, 13) == 'Scalene triangle'
        assert triangle(8, 6, 10) == 'Scalene triangle'

    def test_invalid_triangle(self):
        assert triangle(-8, 100, -0) == 'invalid input'
        assert triangle(0, 0, 0) == 'invalid input'


if __name__ == '__main__':
    
    unittest.main(exit=False, verbosity=2)

