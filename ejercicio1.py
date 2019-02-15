class cuenta():
    def __init__(self,saldo,numero):
        self.saldo=saldo

    def ingreso(self):
        self.saldo=self.saldo+self.numero

    def transferencia(self):
        self.saldo=self.saldo-self.numero

    def reintegro(self):
        self.saldo=self.saldo+numero


    def dame_info(self):
        return self.saldo
