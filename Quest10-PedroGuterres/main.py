from Pessoa import Aluno  
def main():
    aluno = Aluno(1, 'Maria', '222.333.444-20')
    
    print("Informações do Aluno:")
    print(aluno.getmatricula())
    
    aluno.setmatricula(2, 'Ativo')
    print("\nApós atualizar a matrícula:")
    print(f"ID: {aluno.id}, Status: {aluno.status}")
    
    aluno.marcarPresenca()

if __name__ == "__main__":
    main()
