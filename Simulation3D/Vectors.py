import math

class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return  f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Only 3 axis values accessible")

    def __add__(self, other):
        return Vector(self.x+other.x,
                      self.y+other.y,
                      self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x,
                      self.y-other.y,
                      self.z-other.z)

    def __mul__(self, other):

        if isinstance(other, Vector):
            return Vector(self.x * other.x,
                          self.y * other.y,
                          self.z * other.z)

        elif isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other,
                          self.z * other)

        else:
            raise TypeError("Multiplier must be a Vector, integer or a floating point")

    def __truediv__(self, other):

        if isinstance(other, (int, float)):
            return Vector(self.x/other,
                          self.y/other,
                          self.z/other)

        else:
            raise TypeError("Divisor must be an integer or a floating point")

    def get_magnitude(self):
        return math.sqrt( self.x ** 2 + self.y ** 2 + self.z ** 2 )

    def get_unit_vector(self):

        vector_magnitude = self.get_magnitude()

        return Vector(self.x/vector_magnitude,
                      self.y/vector_magnitude,
                      self.z/vector_magnitude)