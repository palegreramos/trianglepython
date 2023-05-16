class Triangulo:

    def __init__(self, base,altura):
        self.base = base
        self.altura=altura

    def area(self):
        return self.base * self.altura / 2
    
    def __str__(self):
        return f"El área del triángulo de base {self.base} y altura {self.altura} es {self.area()}"