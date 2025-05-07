import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

class CadastroProdutos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(100, 100, 400, 300)

        
        self.lista_produtos = []

     
        layout = QVBoxLayout()

       
        self.label_tipo = QLabel("Selecione o tipo de produto:")
        layout.addWidget(self.label_tipo)
        
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Desktop", "Notebook"])
        layout.addWidget(self.combo_tipo)
        self.combo_tipo.currentIndexChanged.connect(self.atualizar_formulario)

       
        self.label_modelo = QLabel("Modelo:")
        layout.addWidget(self.label_modelo)
        self.entry_modelo = QLineEdit()
        layout.addWidget(self.entry_modelo)

        self.label_cor = QLabel("Cor:")
        layout.addWidget(self.label_cor)
        self.entry_cor = QLineEdit()
        layout.addWidget(self.entry_cor)

        self.label_preco = QLabel("Preço:")
        layout.addWidget(self.label_preco)
        self.entry_preco = QLineEdit()
        layout.addWidget(self.entry_preco)

        self.label_categoria = QLabel("Categoria:")
        layout.addWidget(self.label_categoria)
        self.entry_categoria = QLineEdit()
        layout.addWidget(self.entry_categoria)

        
        self.label_extra = QLabel("")
        layout.addWidget(self.label_extra)
        self.entry_extra = QLineEdit()
        layout.addWidget(self.entry_extra)

        
        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(self.botao_cadastrar)

        self.setLayout(layout)
        self.atualizar_formulario()

    def atualizar_formulario(self):
        tipo_produto = self.combo_tipo.currentText()
        if tipo_produto == "Desktop":
            self.label_extra.setText("Potência da Fonte:")
        elif tipo_produto == "Notebook":
            self.label_extra.setText("Tempo de Bateria:")

    def cadastrar(self):
        modelo = self.entry_modelo.text()
        cor = self.entry_cor.text()
        preco = self.entry_preco.text()
        categoria = self.entry_categoria.text()
        extra = self.entry_extra.text()
        tipo = self.combo_tipo.currentText()

        if modelo and cor and preco and categoria and extra:
            categoria_obj = Categoria(1, categoria)  # Criando um objeto Categoria

            if tipo == "Desktop":
                produto = Desktop(modelo, cor, preco, categoria_obj, extra)
            else:
                produto = Notebook(modelo, cor, preco, categoria_obj, extra)

            self.lista_produtos.append(produto)  # Armazena na lista

            QMessageBox.information(self, "Cadastro", f"{tipo} cadastrado com sucesso!\n{produto.getInformacoes()}")
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CadastroProdutos()
    janela.show()
    sys.exit(app.exec_())
