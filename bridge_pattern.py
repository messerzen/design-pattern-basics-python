class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print(f"API 1 drawing a circle at {x}, {y} with radius {radius}")

class DrawingAPITwo(object):
    """Implementation-specific abstarction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing a circle at {x}, {y} with radius {radius}")

class Circle(object):
    """Implementation-independent abstraction: for example, there could"""

    def __init__(self, x, y, radius, drawing_api) -> None:
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation specific abstraction taken care of by another"""

        self._drawing_api.draw_circle(self._x, self._y, self._radius)
             
    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent

if __name__ == "__main__":
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    circle1.draw()

    circle2 = Circle(1, 2, 3, DrawingAPITwo())
    circle2.draw()