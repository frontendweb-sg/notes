import math

class Circle:
    __slots__ = ("r")
    def __init__(self,r) -> None:
        self.r=r;

    @property
    def radius(self):
        return self.r;

    @radius.setter
    def radius(self,r):
        if not isinstance(r, int| float) or r<=0:
            raise TypeError("value type should be int")
        self.r = r;

c = Circle(5)
c.radius=45
c.s = 50;
print(c.radius)
print(c.__slots__)