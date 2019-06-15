class Color:
    def __init__(self, red = 0, green = 0, blue = 0):
        self.r = red
        self.g = green
        self.b = blue

    def red(self):
        return self.r

    def green(self):
        return self.g

    def blue(self):
        return self.b

    def setRed(self, red):
        self.r = red
        return self.r

    def setGreen(self, green):
        self.g = green
        return self.g

    def setBlue(self, blue):
        self.b = blue
        return self.b

    def tuple(self):
        return (self.r, self.g, self.b)

    def list(self):
        return [self.r, self.g, self.b]

    def colorFromList(list):
        return Color(list[0], list[1], list[2])

    def colorFromTuple(tuple):
        return Color(tuple[0], tuple[1], tuple[2])

    def toGray(self):
        avg = int((self.r + self.g + self.b)/3)
        self.r = avg
        self.g = avg
        self.b = avg
        return self
