class Fraction(object):
    def __init__(self, a:int, b:int):#a/b
        self.a = a
        self.b = b
    def __add__(self, other):
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        x, y = a, b
        while b > 0:
            a, b = b, a % b
        x, y = x//a, y//a
        return(Fraction(x, y))
    def __str__(self):
        if self.a == 0:
            return 0
        elif self.b ==1:
            return(str(self.a))
        else:
            return(str(self.a) + "/" + str(self.b))

a1, b1, a2, b2 = map(int, input().split())
x, y = Fraction(a1, b1), Fraction(a2, b2)
print(x + y)