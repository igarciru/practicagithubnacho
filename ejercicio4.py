class alumno():
    def __init__(self,expediente,nombre,nota1,nota2,nota3):
        self.expediente=expediente
        self.nombre=nombre
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3

    def nota_media(self):
        nota_media=(nota1+nota2+nota3)/3
        return nota_media

    def dame_info(self):
        print("Alumno",self.nombre, "con expediente",self.expediente,"tiene una nota media de",self.nota_media)
        if nota_media>=4.8:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")
