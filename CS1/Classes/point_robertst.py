from math import sqrt
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_from_origin(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def distance(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
    def translate(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y
    
    def invert(self):
        self.x = -self.x
        self.y = -self.y
        
    def slope(self, other):
        return ((other.y - self.y) / (other.x - self.x))
    
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        
if __name__ == "__main__":
    p1 = Point(-7, 6)
    p2 = Point(5, -1)
    p3 = Point(3, 4)
    p4 = Point(-2, -6)
    print(p1.quadrant())
    print(p2.quadrant())
    print(p3.quadrant())
    print(p4.quadrant())