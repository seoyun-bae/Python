class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if (self.x + self.width > r.x and self.x < r.x + r.width and
            self.y + self.height > r.y and self.y < r.y + r.height):
            return True
        return False
    
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
if r1.overlap(r2):
    print("r1과 r2는 서로 겹칩니다.")
else:
    print("r1과 r2는 서로 겹치지 않습니다.")