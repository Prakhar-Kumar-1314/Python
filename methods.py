class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_position(self):
        return (self.x, self.y)

    def change_position(self, x_new, y_new):
        self.x = x_new
        self.y = y_new
        return (x_new, y_new)

    def get_area(self):
        cal_area = self.width * self.height
        return cal_area


rect = Rectangle(1, 2, 10, 12)
pos = rect.get_position()

pos = rect.change_position(2, 4)
print(pos)

area = rect.get_area()

print(area)
