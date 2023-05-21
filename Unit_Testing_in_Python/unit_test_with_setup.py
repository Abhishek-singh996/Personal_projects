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

class TestGetAreaRectangleWithSetUp(unittest.TestCase):
    def setUp(self):
        self.rectangle = Area(0, 0)
    
    def test_normal_case(self):
        self.rectangle.set_width(2)
        self.rectangle.set_height(3)
        self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")
    
    def test_negative_case(self): 
        """expect -1 as output to denote error when looking at negative area"""
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "incorrect negative output")

unittest.main()
