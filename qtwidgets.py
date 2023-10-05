import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Exit')
botao.setStyleSheet('font-size: 40px;')
# Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Exit2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Exit3')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()
layout = QGridLayout()
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)
central_widget.show()
central_widget.setLayout(layout)
app.exec()  # O loop da aplicação

# e possivel configurar o Qgrid por linha e coluna o que pode ser mais
# vantajoso podendo colocar tanto na vertical como na horizontal
# sendo possivel tambem expandir um botao por duas colunas ou linhas

# o Qvertical organiza os widgets na vertical automaticamente
# o Qhorizontal organiza os widgets na horizontal automaticamente
