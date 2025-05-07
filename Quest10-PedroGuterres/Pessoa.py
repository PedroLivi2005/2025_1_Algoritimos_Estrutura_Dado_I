from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self._cpf = cpf

    @abstractmethod
    def marcarPresenca(self):
        pass
    
    def __matricula(self): 
        return f"Nome: {self.nome}\nCPF: {self._cpf}"
    
    def getmatricula(self):
        return self.__matricula()
    
    def setmatricula(self, id, status):
        if id > 0: 
            self.id = id
            self.status = status

class Aluno(Pessoa):
    def marcarPresenca(self):
        print(f"{self.nome} marcou presença.")
    
    def __matricula(self):
        return self.__matricula()
         

aluno = Aluno(1, 'Maria', '222.333.444-20')
print(aluno.getmatricula())
aluno.setmatricula(2, 'Ativo')
print(aluno.id, aluno.status)
