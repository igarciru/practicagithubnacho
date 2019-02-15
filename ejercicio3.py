class contador():
    def __init__(self,numero):
        self.numero=numero

    def get_valor(self):
        return self.numero

    def sube(self):
        self.numero=self.numero+1

    def baja(self):
        self.numero=self.numero-1

contador0=contador(0)
contador0.sube()
print(contador0.get_valor())
