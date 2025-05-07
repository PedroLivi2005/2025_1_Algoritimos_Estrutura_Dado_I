from Produto import Produto

class Notebook(Produto):
    
    def __init__(self, modelo, cor, preco, categoria,  tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self.__tempoDeBateria}"


    def get_tempoDeBateria(self):
        return self.__tempoDeBateria
    
    
    def set_tempoDeBateria(self, tempoDeBateria):
        if tempoDeBateria >= 0 :
            self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        print(f"Notebook {self.modelo} cadastrado com sucesso!")

