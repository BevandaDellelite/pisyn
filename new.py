from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QListWidget
from PyQt5.QtCore import Qt 

app = QApplication([])
window = QWidget()


line = QLineEdit()
list1 = QListWidget()

b1 = QPushButton('dobavyty')
toma = QPushButton('vidalyty')
taras = QPushButton('zberegty')\

v1 = QVBoxLayout()
v1.addWidget(line)
v1.addWidget(b1)
v1.addWidget(list1)
v1.addWidget(toma)
v1.addWidget(taras)

taras2 = []
def add():
    t = line.text()#go go go go
    if t:
        taras2.append(t)
        list1.addItem(t)
        line.clear()
b1.clicked.connect(add)

def delete():
    t = list1.currentRow()
    if t>=0:
        del taras2[t]
toma.clicked.connect(delete)

def save():
    with open('tasks.txt',"w") as f:
        for t in taras2:
            f.write(t+'\n')
taras.clicked.connect(save)
window.setLayout(v1)
window.show()
app.exec_()