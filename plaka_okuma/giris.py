# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from anasayfa import Ui_MainWindow
class Ui_Anasayfa(object):
    def Kontrol(self):
        admin_adi=self.giris_adi_input.text()
        admin_sifre= self.giris_sifre_input.text()
        if admin_adi=="" and admin_sifre=="":
            self.hata('Kullanıcı adı ve Şifre Hatası', 'Lütfen mail adresinizi ve Şifrenizi giriniz.')
        elif admin_adi == "":
            self.hata('Kullanıcı Adı Hatası','Lütfen mail adresinizi giriniz')
        elif admin_sifre=="":
            self.hata('Şifre Hatası','Lütfen Şifrenizi giriniz.')
        else:
            baglan = sqlite3.connect("veritabanı.db")
            kontrol = baglan.execute("SELECT * FROM ADMIN WHERE ADMIN_ADI = ? AND ADMIN_SIFRE = ?", (admin_adi,admin_sifre))
            sorgu = kontrol.fetchall()

            if (sorgu): # email adresi kayıtlı mı?
                if sorgu[0][2] == admin_sifre:  # [0]=ip,mail,sifre. [2]=sifre
                    self.openWindow()
                else:
                    self.hata('Şifre Hata!', 'Şifrenizi doğru değil.')
            else:
                self.hata('Hata!', 'Kullanıcı Kayıtlı Değil...')

            baglan.commit()
            baglan.close()
    def hata(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def openWindow(self):
        self.window= QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        Anasayfa.hide()
        self.window.show()

    def setupUi(self, Anasayfa):
        Anasayfa.setObjectName("Anasayfa")
        Anasayfa.resize(564, 803)
        Anasayfa.setFixedSize(564,803)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Anasayfa.sizePolicy().hasHeightForWidth())
        Anasayfa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Anasayfa.setFont(font)
        Anasayfa.setAccessibleDescription("")
        Anasayfa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Anasayfa)
        self.label.setGeometry(QtCore.QRect(20, 10, 441, 361))
        self.label.setStyleSheet("background-image: url(:/newPrefix/grc/2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Anasayfa)
        self.frame.setGeometry(QtCore.QRect(20, 410, 501, 281))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 70, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 31, 16))
        self.label_4.setObjectName("label_4")
        self.giris_adi_input = QtWidgets.QLineEdit(self.frame)
        self.giris_adi_input.setGeometry(QtCore.QRect(190, 61, 221, 41))
        self.giris_adi_input.setObjectName("giris_adi_input")
        self.giris_sifre_input = QtWidgets.QLineEdit(self.frame)
        self.giris_sifre_input.setGeometry(QtCore.QRect(190, 120, 221, 41))
        self.giris_sifre_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris_sifre_input.setObjectName("giris_sifre_input")
        self.giris_yap_btn = QtWidgets.QPushButton(self.frame)
        self.giris_yap_btn.setGeometry(QtCore.QRect(250, 200, 121, 31))
        self.giris_yap_btn.setCheckable(False)
        self.giris_yap_btn.setObjectName("giris_yap_btn")
        ########Yönlendirme#######
        self.giris_yap_btn.clicked.connect(self.Kontrol)

        self.retranslateUi(Anasayfa)
        QtCore.QMetaObject.connectSlotsByName(Anasayfa)

    def retranslateUi(self, Anasayfa):
        _translate = QtCore.QCoreApplication.translate
        Anasayfa.setWindowTitle(_translate("Anasayfa", "Giriş Sayfası"))
        self.label_3.setText(_translate("Anasayfa", "Kullanıcı Adı"))
        self.label_4.setText(_translate("Anasayfa", "Şifre"))
        self.giris_yap_btn.setText(_translate("Anasayfa", "Giriş Yap"))

import xy

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Anasayfa = QtWidgets.QDialog()
    ui = Ui_Anasayfa()
    ui.setupUi(Anasayfa)
    Anasayfa.show()
    sys.exit(app.exec_())

