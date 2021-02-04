class shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        print("계산할 수 없음!")
    
    def perimeter(self):
        print("계산할 수 없음!")
    
class Rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h
    
    def perimeter(self):
        return 2*(self.w + self.h)

a = Rectangle(0,0,30,50)

print("사각형의 넓이는 : {0}".format(a.area()))
print("사각형의 둘레는 : {0}".format(a.perimeter()))