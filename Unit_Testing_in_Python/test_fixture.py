import pytest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

@pytest.fixture(scope='class')
def rectangle():
    return Rectangle(0, 0)
 
def test_negative_case(rectangle):
    print (rectangle.width)
    rectangle.set_width(-1)
    rectangle.set_height(2)
    assert rectangle.get_area() == -1, "incorrect negative output"
 
## for test the code run the code in command line    .....File name should be start with 'test' prefix

'''
pytest test_fixture.py
'''