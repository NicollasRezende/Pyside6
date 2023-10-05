### GUIA Basico de como usar a biblioteca Pyside6 Python:
# _______________________________________
# Meu Projeto Pyside6

## Este é um exemplo de projeto que utiliza a biblioteca Pyside6 para criar interfaces gráficas em Python.
### Instalação

  Para instalar o Pyside6, execute:


    pip install pyside6

- Certifique-se de ter o Python 3.6 ou superior instalado.

# _______________________________________

# Exemplo Básico:

## Aqui está um exemplo simples criando uma janela com Pyside6:



    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    
    window = QMainWindow()
    window.show()
    
    app.exec()

### Esse código cria uma instância QApplication, uma janela QMainWindow e exibe essa janela.

  - O loop *app.exec()* executa a aplicação.

# _______________________________________

# Criando Widgets

## Pyside6 permite criar e organizar vários widgets, como botões, caixas de texto e muito mais.

### Aqui está um exemplo adicionando um botão e uma caixa de texto:



    btn = QPushButton("Clique Aqui") 
    txt = QLineEdit()
    
    layout = QVBoxLayout()
    layout.addWidget(btn)
    layout.addWidget(txt)
    
    window.setLayout(layout)

# _______________________________________

# Sinais e Slots

## Um recurso importante do Pyside é o sistema de sinais e slots que permite aos widgets se comunicarem.

### Aqui conectamos o sinal clicked do botão a um método:



    btn.clicked.connect(self.clicou_botao)
    
    def clicou_botao(self):
      print("Botão clicado!")

- Isso imprime uma mensagem quando o botão for clicado.

# _______________________________________

# Resumo

**Essa é uma introdução básica ao Pyside6 para criar interfaces gráficas em Python. Há muitos outros widgets e recursos avançados disponíveis para construir aplicativos GUI complejos. Para mais Informaçoes Click no link abaixo**

- ***https://doc.qt.io/qtforpython-6/quickstart.html***
