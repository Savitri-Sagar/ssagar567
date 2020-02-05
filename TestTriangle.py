''' Test the program of classifying triangle'''
import unittest
from Triangle import triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_classify_triangle(self):
        res = triangle(1,1,1)
        self.assertEqual(res, "equilateral")
        
        res1 = triangle(1,1,2)
        self.assertEqual(res1, "isosceles")

        res2 = triangle(1,2,3)
        self.assertEqual(res2, "scalene")

        res3 = ctriangle(3,4,5)
        self.assertEqual(res3, "right angle triangle")
        
        res4 = triangle(0,0,0)
        self.assertEqual(res4, "Invalid Input")

if __name__ == '__main__':
    unittest.main()
