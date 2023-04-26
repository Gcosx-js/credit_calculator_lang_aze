from PyQt5.QtWidgets import *
from pencere import Ui_Form
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtWidgets, QtGui

class Ekran(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1103, 441)
        self.app1 = Ui_Form()
        self.app1.setupUi(self)
        self.app1.mebled_slider.valueChanged.connect(self.mebleg_slider)
        self.app1.lineEdit_mebleg.textChanged.connect(self.mebleg_lineEdit)
        self.app1.muddet_slider.valueChanged.connect(self.muddet_slider)
        self.app1.lineEdit_muddet.textChanged.connect(self.muddet_lineedit)
        self.app1.faiz_slider.valueChanged.connect(self.faiz_slider)
        self.app1.lineEdit_faiz.textChanged.connect(self.faiz_lineedit)
        self.app1.hesabla_button.clicked.connect(self.hesabla)
        self.lineedit_mebleg = self.app1.lineEdit_mebleg
        self.lineedit_muddet = self.app1.lineEdit_muddet
        self.lineedit_faiz = self.app1.lineEdit_faiz

        # Tam sayılar için validator oluşturun
        integer_validator = QtGui.QIntValidator()

        # LineEdit widget'larınız için validator'ları ayarlayın
        self.lineedit_mebleg.setValidator(integer_validator)
        self.lineedit_muddet.setValidator(integer_validator)
        self.lineedit_faiz.setValidator(integer_validator)
        
    
    def mebleg_lineEdit(self,value):
        
        if value=="":
            self.app1.mebled_slider.setValue(0)
        else:
            v = int(value)
            self.app1.mebled_slider.setValue(v)
 
    def mebleg_slider(self,value):
        self.app1.kredit_meglegi_label.setText(str(value))
        self.app1.lineEdit_mebleg.setText(str(value))
    
    def muddet_lineedit(self,value):
        
        if value=="":
            self.app1.muddet_slider.setValue(0)
        else:
            v = int(value)
            self.app1.muddet_slider.setValue(v)
 
    def muddet_slider(self,value):
        self.app1.kredit_muddeti_label.setText(str(value))
        self.app1.lineEdit_muddet.setText(str(value))
    
    
    def faiz_lineedit(self,value):
        if value =="":
            self.app1.faiz_slider.setValue(0)
            self.app1.lineEdit_faiz.setText(str(0))
        else:
            v = int(value)
            self.app1.faiz_slider.setValue(v)
            self.app1.lineEdit_faiz.setText(str(v))

    
    def faiz_slider(self,value):
        v= int(value)
        self.app1.faiz_derecesi_label.setText(str(v))
        self.app1.lineEdit_faiz.setText(str(v))
    
    
    def hesabla(self):
        if self.app1.lineEdit_muddet.text() == "" or self.app1.lineEdit_mebleg.text() == "0":
            self.app1.ayllq_odenis_label.setText("None")
            self.app1.umumi_mebleg_label.setText("None")
        else: # eger içeride deyerler varsa bura girsin
            if self.app1.faiz_slider.value() != 0:
                self.umumi = ((int(self.app1.kredit_meglegi_label.text()) * int(self.app1.faiz_derecesi_label.text())) / 100) + int(self.app1.kredit_meglegi_label.text())
                self.app1.ayllq_odenis_label.setNum(round(float(self.umumi/int(self.app1.kredit_muddeti_label.text())), 1))
                self.app1.umumi_mebleg_label.setNum(round((self.umumi),1))


            else:
                self.umumi = int(self.app1.kredit_meglegi_label.text())
                self.app1.umumi_mebleg_label.setNum(round((self.umumi),1))
                self.app1.ayllq_odenis_label.setNum(round(float(self.umumi/int(self.app1.kredit_muddeti_label.text())),1))


                
                
app = QApplication([])
ekran = Ekran()
ekran.show()
app.exec_()
