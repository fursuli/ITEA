class Point:

    def __init__(self, x, y, z):
        self._x_coo = x
        self._y_coo = y
        self._z_coo = z
        self.coordinates = (self._x_coo, self._y_coo, self._z_coo)

    def get_x(self):
        return self._x_coo

    def set_x(self, value):
        self._x_coo = value

    def get_y(self):
        return self._y_coo

    def set_y(self, value):
        self._y_coo = value

    def get_z(self):
        return self._z_coo

    def set_z(self, value):
        self._z_coo = value

    def __add__(self, other):
        return Point(
            self._x_coo + other._x_coo,
            self._y_coo + other._y_coo,
            self._z_coo + other._z_coo
        )

    def __sub__(self, other):
        return Point(
            self._x_coo - other._x_coo,
            self._y_coo - other._y_coo,
            self._z_coo - other._z_coo
        )

    def __mul__(self, other):
        return Point(
            self._x_coo * other._x_coo,
            self._y_coo * other._y_coo,
            self._z_coo * other._z_coo
        )

    def __truediv__(self, other):

        if 0 in other.coordinates:
            print(f"I can't divide by zero, which is in {other.coordinates}")
            return Point(0,0,0)
        else:
            return  Point(
                self._x_coo / other._x_coo,
                self._y_coo / other._y_coo,
                self._z_coo / other._z_coo
                )


a = Point(1,2,3)
print(a.coordinates)

b = a.__mul__(a)
print(b.coordinates)

c = a.__add__(a)
print(c.coordinates)

d = b.__sub__(a)
print(d.coordinates)

e = b.__truediv__(d)
print(e.coordinates)