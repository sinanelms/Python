import sys
from PyQt5 import QtWidgets, QtGui
def Pencere():
    app =   QtWidgets.QApplication(sys.argv)
    okay =  QtWidgets.QPushButton("Tamam")

    cancel = QtWidgets.QPushButton("İptal")
    h_box =QtWidgets.QHBoxLayout()    #v_box= QtWidgets.QVBox^Layout()(üstsüteolue)
    h_box.addWidget(okay)              #v_box.addWidget(okay)
    h_box.addWidget(cancel)             #v_box.addWidget(cancel)
    h_box.addStretch()



    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders4")
    pencere.setLayout(h_box)                #v_box

    pencere.setGeometry(100, 100, 500, 500)






    pencere.show()
    sys.exit((app.exec_()))


Pencere()