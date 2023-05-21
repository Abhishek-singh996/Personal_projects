import unittest

class Area:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width*self.height
    
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    
class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectangle = Area(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
    def test_negative_case(self): 
        """expect -1 as output to denote error when looking at negative area"""
        rectangle = Area(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative output")

unittest.main()



        