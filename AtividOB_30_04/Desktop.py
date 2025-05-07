from Produto import Produto

class Desktop(Produto):
    
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potência da Fonte: {self._potenciaDaFonte}"

    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte

    def set_potenciaDaFonte(self, potencia):
        if potencia > 0:
            self._potenciaDaFonte = potencia
    
    def cadastrar(self):
        print(f"Desktop {self.modelo} cadastrado com sucesso!")

        