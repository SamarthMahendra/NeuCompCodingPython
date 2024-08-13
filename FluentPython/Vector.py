import math
class Vector:

     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y

     def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

     def __abs__(self):
        return math.hypot(self.x, self.y)

     def __bool__(self):
         return bool(abs(self))

     def __add__(self, other):
         x = self.x + other.x
         y = self.y + other.y
         return Vector(x, y)

     def __mul__(self, other):
         if isinstance(other, int):
             return Vector(self.x * other, self.y * other)
         else:
             # get angle and then use vector multiplication
            magnitude = abs(self)
            angle = math.atan2(self.y, self.x)
            new_magnitude = magnitude * scalar



     def __eq__(self, other):
         return self.x == other.x and self.y == other.y


     def __hash__(self):
         return hash(self.x) ^ hash(self.y)


# testing
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)  # Output: Vector(4, 5)
print(v1 * 3)  # Output: Vector(6, 12)
print(abs(Vector(3, 4)))  # Output: 5.0

