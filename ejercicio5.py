import random
class rectangulo():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def dame_perimetro(self):
        self.perimetro=2*self.base+2*self.altura
        return self.perimetro

    def dame_area(self):
        self.area=self.base*self.altura
        return self.area 


class prueba_rectangulo(rectangulo):
    def __init__(self):
        super().__init__(base,altura)

    def pruebas(self):
        for i in range(10):
            self.base=random.randrange(100)
            self.altura=random.randrange(100)
            print(dame_perimetro)
            print(dame_area)
