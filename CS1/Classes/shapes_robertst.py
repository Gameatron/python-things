from point_robertst import *
class Rectangle:
    def __init__(self, point, width, height):
        self.point = point
        self.width = abs(width)
        self.height = abs(height)
        
    def __str__(self):
        return f"{self.point},w={self.width},h={self.height}"
    
    def translate(self, shift_x, shift_y):
        self.point.translate(shift_x, shift_y)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
    def bottom_right(self):
        return Point(self.point.x+self.width, self.point.y-self.height)
    
    def bottom_left(self):
        return Point(self.point.x, self.point.y+self.height)
    
    def top_right(self):
        return Point(self.point.x+self.width, self.point.y)
    
    def center(self):
        return Point(self.point.x+self.width/2, self.point.y-self.height/2)
    
    def inside(self, point):
        if (point.x >= self.point.x and point.x <= self.bottom_right().x) and (point.y <= self.point.y and point.y >= self.bottom_right().y):
            return True
        else:
            return False
        
    def overlap(self, other):
        # Checks if other is inside of self
        if self.inside(other.point) == True and self.inside(other.bottom_left()) == True and self.inside(other.bottom_right()) == True and self.inside(other.top_right()) == True:
            return other

        # Checks if self is inside of other
        elif other.inside(self.point) == True and other.inside(self.bottom_left()) == True and other.inside(self.bottom_right()) == True and other.inside(self.top_right()) == True:
            return self
        
        # Checks if the top left point of self is inside of other
        elif other.inside(self.point) == True and other.inside(self.bottom_left()) == False and other.inside(self.bottom_right()) == False and other.inside(self.top_right()) == False:
            height = None
            width = None
            return Rectangle(self.point, 1, 1)
        
        # Checks if the top left point of other is inside of self
        elif self.inside(other.point) == True and self.inside(other.bottom_left()) == False and self.inside(other.bottom_right()) == False and self.inside(other.top_right()) == False:
            return Rectangle(other.point, 1, 1)

        
class Circle:
    def __init__(self, center, edge):
        self.center = center
        self.edge = edge
    
    def get_radius(self):
        return self.center.distance(self.edge)
    
    def __str__(self):
        return f"Center: {self.center}\tRadius:{self.get_radius()}"

    def area(self):
        return 3.14*self.get_radius()**2
    
    def circumfrence(self):
        return 3.14*(self.get_radius()*2)
    
def main():
    p1 = Point(-2, 4)
    p2 = Point(0, 2)
    r1 = Rectangle(p1, 8, 4)
    r2 = Rectangle(p2, 8, 4)
    print(r1)
    print(r2)
    print(r1.inside(r2.point))
    print(r1.overlap(r2))
  #  print(r1)
  #  print(r1.area())
  #  print(r1.perimeter())
  #  print(r1.bottom_right())
  #  print(r1.center())
    
  #  p2 = Point(5, 8)
  #  c1 = Circle(p1, p2)
  #  print(c1.get_radius())
  #  print(c1)
  #  print(c1.area())
  #  print(c1.circumfrence())

if __name__ == "__main__":
    main()