class TriangleChecker():
    def __init__(self,a,b,c):
        self.a , self.b , self.c = a,b,c
        
    def is_triangle(self):  
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        elif self.a < self.b + self.c or self.b < self.c + self.a or self.c < self.a + self.b:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

triangle=TriangleChecker(-1,2,3)
print(triangle.is_triangle())