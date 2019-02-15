class libro():
    def __init__(self,lotengo,nolotengo):
        self.lotengo=lotengo
        self.nolotengo=nolotengo

    def prestamo(self):
        self.lotengo=0
        self.nolotengo=1

    def devolucion(self):
        self.nolotengo=0
        self.lotengo=1

    def dame_info(self):
        if self.lotengo==1:
            print("Tengo el libro")

        else:
            print("Lo he prestado")
