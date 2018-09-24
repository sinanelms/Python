
import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    li = QtWidgets.QLabel(w)
    li.setText("Merhaba")
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Pencere')
    w.show()

    sys.exit(app.exec_())
window()