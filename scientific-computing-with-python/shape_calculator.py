class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle(width={0}, height={1})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        output = str()
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for y in range(self.height):
            for x in range(self.width):
                output = output + "*"
            output = output + "\n"
        return output

    def get_amount_inside(self, shape):
        width = shape.width
        height = shape.height
        x = int(self.width / width)
        y = int(self.height / height)
        return x * y

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __repr__(self):
        return "Square(side={0})".format(self.width)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
