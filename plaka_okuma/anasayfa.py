# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import IPwebcam
class Ui_MainWindow(object):

    def Kullanici_Ekle(self):

        self.k_adi=self.k_adi_input.text()
        self.k_sifre=self.k_sifre_input.text()

        if str(self.k_durum_comboBox.currentText())=="Aktif":
            self.k_durum ="1"
        else:
            self.k_durum="2"


        if self.k_adi=="" and self.k_sifre=="":
            self.hata('Kullanıcı Adı ve Şifre Hatası', 'Lütfen Kullanıcı Adı ve Şifre giriniz.')
        elif self.k_adi=="":
            self.hata('Kullanıcı Ad Hatası', 'Lütfen Kullanıcı Adı Giriniz.')
        elif self.k_sifre=="":
            self.hata('Kullanıcı Sifre Hatası','Lütfen Kullanıcı Sifre Giriniz.')
        else:
            baglan=sqlite3.connect("veritabanı.db")
            # cursor tablodaki satır sayısı
            cursor = baglan.cursor()
            cursor.execute('SELECT COUNT(*) FROM KULLANICILAR')
            rowcount = str(cursor.fetchone()[0])
            ################
            baglan.execute("INSERT INTO KULLANICILAR VALUES(?,?,?,?)", (rowcount,self.k_adi,self.k_sifre,self.k_durum))
            baglan.commit()
            baglan.close()
            self.k_adi_input.clear() #clear içerisini temizliyor
            self.k_sifre_input.clear()
            self.kullanici_tablo()
        self.k_adi=""
        self.k_sifre=""
        self.k_durum=""

    def IP_Ekle(self):
        self.comboboxclear()
        ip_adres=self.ip_adres_ekle_input.text()
        ip_adi=self.ip_adi_ekle_input.text()
        if ip_adres=="" and ip_adi=="":
            self.hata('Kullanıcı Adı ve Şifre Hatası', 'Lütfen Kullanıcı Adı ve Şifre giriniz.')
        elif ip_adres=="":
            self.hata('Kullanıcı Ad Hatası', 'Lütfen Kullanıcı Adı Giriniz.')
        elif ip_adi=="":
            self.hata('Kullanıcı Sifre Hatası','Lütfen Kullanıcı Sifre Giriniz.')
        else:
            baglan=sqlite3.connect("veritabanı.db")
            # cursor tablodaki satır sayısı
            cursor = baglan.cursor()
            cursor.execute('SELECT COUNT(*) FROM IP')
            rowcount = str(cursor.fetchone()[0])
             ################
            a=baglan.execute("INSERT INTO IP VALUES(?,?,?)", (rowcount,ip_adres,ip_adi))
            son_id=a.lastrowid
            baglan.commit()
            baglan.close()
            self.ip_adres_ekle_input.clear() #clear içerisini temizliyor
            self.ip_adi_ekle_input.clear()
            #self.IP_Listeleme(son_id)
            self.clear()
            self.IP_yenileme()
        self.combobox()
    def Kontrol(self,ip_adres,ip_adi):
        baglan = sqlite3.connect("veritabanı.db")
        a= baglan.execute("SELECT * FROM IP")
        sorgu=a.fetchall()
        b=True
        for i in sorgu:
            if i[1]==ip_adres or i[2]==ip_adi:
                b=False
            else:
                b=True
        return b
        baglan.commit()
        baglan.close()
    #############
    def IP_Listeleme(self,son_id):
        baglan = sqlite3.connect("veritabanı.db")
        aa= baglan.execute("SELECT IP_ADI FROM IP WHERE ID=?",(str((int(son_id)-1)),))
        ad=aa.fetchone()[0] #felchall veri okuma
        item = QtWidgets.QListWidgetItem(ad)
        self.listWidget.addItem(item)
        baglan.commit()
        baglan.close()


    def IP_yenileme(self):
        baglan = sqlite3.connect("veritabanı.db")
        sayac = 0
        oku = baglan.execute("SELECT IP_ADI FROM IP")
        for verilericek in oku.fetchall():
            item = QtWidgets.QListWidgetItem(verilericek[0])
            self.listWidget.addItem(item)
            sayac += 1
        baglan.commit()
        baglan.close()
    def clear(self):
        self.listWidget.clear()


    def item_click(self, item):
        self.secili=str(item.text())


    def sil(self):
        #self.clear()
        self.comboboxclear() # combobox verileri temizliyor. en aşağıda tekrar combobox listeneliyor. yenileme
        baglan = sqlite3.connect("veritabanı.db")
        sorgu = baglan.execute("SELECT IP_ADI FROM IP")

        aaa=self.secili

        if aaa=="":
            self.hata('Silme Hatası', 'Lütfen Silmek istediğini IP adını seçiniz')
        else:
            self.clear()
            for i in sorgu.fetchall():
                if i[0]==self.secili:
                    baglan.execute("DELETE FROM IP WHERE IP_ADI=?",(self.secili,))
                    self.clear()
            self.clear()
        baglan.commit()
        baglan.close()
        self.IP_yenileme() # ip sildikten sonra listenin yukardaki clear ile temizlenip tekrar listelenmesi
        self.combobox() #combobox yukarda clear ile temizledi. burda yeniden listeneleniyor.
    def hata(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def combobox(self):
        baglan = sqlite3.connect("veritabanı.db")
        oku = baglan.execute("SELECT IP_ADI FROM IP")
        for verilericek in oku.fetchall():
            self.baslat_comboBox.addItem(verilericek[0])
        baglan.commit()
        baglan.close()
    def comboboxclear(self):
        self.baslat_comboBox.clear()

    def combo_input(self):
        self.combobox_text = str(self.baslat_comboBox.currentText())
        baglan = sqlite3.connect("veritabanı.db")
        sorgu = baglan.execute("SELECT IP_ADRES FROM IP WHERE IP_ADI=?", (self.combobox_text,))
        self.baslat_ip_input.setText(sorgu.fetchone()[0])
        baglan.commit()
        baglan.close()


    def pass_Net_Adap(self):
        self.combo_secili=str(self.baslat_comboBox.currentText())
        baglan = sqlite3.connect("veritabanı.db")
        sorgu = baglan.execute("SELECT IP_ADRES FROM IP WHERE IP_ADI=?",(self.combo_secili,))
        self.baslat_ip_input.setText(sorgu.fetchone()[0])
        baglan.commit()
        baglan.close()
        #self.baslat_ip_input.setText(self.combo_secili)
       ###################################################### print(self.baslat_ip_input.text())
    def IP_Baslat(self):
        url=self.baslat_ip_input.text()
        IPwebcam.islem(url)

    def IP_Duzenle(self):
        self.clear()
        baglan = sqlite3.connect("veritabanı.db")
        sorgu_ad = baglan.execute("SELECT IP_ADI FROM IP WHERE IP_ADI=?", (self.secili,))
        self.ip_adi_ekle_input.setText(sorgu_ad.fetchone()[0]) # input alanına deger gönderiyor.
        sorgu_adres=baglan.execute("SELECT IP_ADRES FROM IP WHERE IP_ADI=?", (self.secili,))
        self.ip_adres_ekle_input.setText(sorgu_adres.fetchone()[0])
        baglan.execute("DELETE FROM IP WHERE IP_ADI=?", (self.secili,))
        baglan.commit()
        baglan.close()
        self.IP_yenileme()

    def kullanici_tablo(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem("Kullanıcı Adı")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem("Kullanıcı Sifre")
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem("Durumu")
        self.tableWidget.setItem(0, 2, item)
        baglan = sqlite3.connect("veritabanı.db")
        sorgu = baglan.execute("SELECT * FROM KULLANICILAR")
        vericek = sorgu.fetchall()  # felchall veri okuma toplu olarak okur
        for index, veri in enumerate(vericek):
            # Tablonun altında boş bir satır oluştur
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            # Satıra metin ekle
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(veri[1]))
            self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(veri[2]))
            if veri[3]=="1":
                self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem("Aktif"))
            else:
                self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem("Pasif"))
        baglan.commit()
        baglan.close()

    def Kullanici_Duzenle(self):
        secili_tablo=self.secili_tablo
        if secili_tablo!=None:
            self.tableWidget.clear()
            self.tableWidget.setRowCount(1)
            item = QtWidgets.QTableWidgetItem("Kullanıcı Adı")
            self.tableWidget.setItem(0, 0, item)
            item = QtWidgets.QTableWidgetItem("Kullanıcı Sifre")
            self.tableWidget.setItem(0, 1, item)
            item = QtWidgets.QTableWidgetItem("Durumu")
            self.tableWidget.setItem(0, 2, item)
            baglan = sqlite3.connect("veritabanı.db")
            sorgu_adi = baglan.execute("SELECT K_ADI FROM KULLANICILAR WHERE K_ADI=?", (secili_tablo,))
            self.k_adi_input.setText(sorgu_adi.fetchone()[0])  # input alanına deger gönderiyor.
            sorgu_sifre = baglan.execute("SELECT K_SIFRE FROM KULLANICILAR WHERE K_ADI=?", (secili_tablo,))
            self.k_sifre_input.setText(sorgu_sifre.fetchone()[0])  # input alanına deger gönderiyor.
            baglan.execute("DELETE FROM KULLANICILAR WHERE K_ADI=?", (secili_tablo,))
            baglan.commit()
            baglan.close()
            self.kullanici_tablo()
        else:
            self.hata('Seçme Hatası', 'Lütfen Duzenlemek için Tablodan seçiniz..')





    def tablo_click(self, item):
        self.secili_tablo = str(item.text())

    def Kullanici_Sil(self):
        self.hata('Uyarı', 'Yapım Aşamasında')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 160, 361, 341))
        self.listWidget.setObjectName("listWidget")

        ##################33
        self.clear()
        self.IP_yenileme()

        #self.listWidget.itemSelectionChanged.connect

        self.listWidget.itemClicked.connect(self.item_click)
        #item = QtWidgets.QListWidgetItem()
        #self.listWidget.addItem(item)
        #item = QtWidgets.QListWidgetItem()
        #self.listWidget.addItem(item)
        self.ip_duzenle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ip_duzenle_btn.setGeometry(QtCore.QRect(10, 500, 101, 28))
        self.ip_duzenle_btn.setObjectName("ip_duzenle_btn")
        # Secili ip düzenleme butonuna tıklayonca
        self.ip_duzenle_btn.clicked.connect(self.IP_Duzenle)


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(402, 11, 541, 81))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 40, 55, 16))
        self.label_3.setObjectName("label_3")
        self.baslat_ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.baslat_ip_input.setGeometry(QtCore.QRect(670, 31, 261, 31))
        self.baslat_ip_input.setObjectName("baslat_ip_input")
        #################################

        self.baslat_btn = QtWidgets.QPushButton(self.centralwidget)
        self.baslat_btn.setGeometry(QtCore.QRect(570, 100, 93, 28))
        self.baslat_btn.setObjectName("baslat_btn")
        self.baslat_btn.clicked.connect(self.IP_Baslat)

        self.durdur_btn = QtWidgets.QPushButton(self.centralwidget)
        self.durdur_btn.setGeometry(QtCore.QRect(670, 100, 93, 28))
        self.durdur_btn.setObjectName("durdur_btn")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(12, 10, 351, 121))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEnabled(False) ### giriş engelleme
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label_5.setObjectName("label_5")
        self.ip_adres_ekle_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_adres_ekle_input.setGeometry(QtCore.QRect(100, 20, 251, 22))
        self.ip_adres_ekle_input.setObjectName("ip_adres_ekle_input")
        self.ip_adi_ekle_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_adi_ekle_input.setGeometry(QtCore.QRect(100, 60, 161, 22))
        self.ip_adi_ekle_input.setObjectName("ip_adi_ekle_input")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 60, 41, 16))
        self.label_6.setObjectName("label_6")
        self.ip_ekle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ip_ekle_btn.setGeometry(QtCore.QRect(100, 90, 93, 28))
        self.ip_ekle_btn.setObjectName("ip_ekle_btn")
        # ip ekle butonuna tıklayınca
        self.ip_ekle_btn.clicked.connect(self.IP_Ekle)

        ################33
        ''' self.baslat_comboBox.setItemText(0, _translate("MainWindow", "IP Seçili Değil"))
        self.baslat_comboBox.setItemText(1, _translate("MainWindow", "Engin"))
        self.baslat_comboBox.setItemText(2, _translate("MainWindow", "Demet"))'''

        '''item = QtWidgets.QListWidgetItem(verilericek[0])
        self.listWidget.addItem(item)
        QtWidgets.QListWidget
        '''

        self.baslat_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.baslat_comboBox.setGeometry(QtCore.QRect(470, 40, 111, 22))
        self.baslat_comboBox.setObjectName("baslat_comboBox")
       ########################
        self.comboboxclear()
        self.combobox()
        self.combo_input()
        self.baslat_comboBox.activated.connect(self.pass_Net_Adap)

        self.ip_sil_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ip_sil_btn.setGeometry(QtCore.QRect(110, 500, 91, 28))
        self.ip_sil_btn.setObjectName("ip_sil_btn")
        ###### seçili listedeli ip silme
        self.ip_sil_btn.clicked.connect(self.sil)


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 160, 541, 401))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 170, 121, 16))
        self.label_4.setObjectName("label_4")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(430, 190, 431, 181))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")


        item = QtWidgets.QTableWidgetItem("Kullanıcı Adı")
        self.tableWidget.setItem(0,0,item)
        item = QtWidgets.QTableWidgetItem("Kullanıcı Sifre")
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem("Durumu")
        self.tableWidget.setItem(0, 2, item)
        self.kullanici_tablo()
        self.tableWidget.itemClicked.connect(self.tablo_click)
        #item = QtWidgets.QTableWidgetItem("engin")
        #self.tableWidget.setItem(0,0,item)
        #item = QtWidgets.QTableWidgetItem("engin")
        #self.tableWidget.setItem(0, 1, item)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 430, 511, 121))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 440, 71, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7.setEnabled(False)
        self.k_adi_input = QtWidgets.QLineEdit(self.centralwidget)
        self.k_adi_input.setGeometry(QtCore.QRect(540, 440, 171, 22))
        self.k_adi_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.k_adi_input.setObjectName("k_adi_input")


        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 440, 55, 16))
        self.label_9.setObjectName("label_9")
        self.k_durum_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.k_durum_comboBox.setGeometry(QtCore.QRect(790, 440, 121, 22))
        self.k_durum_comboBox.setObjectName("k_durum_comboBox")
        self.k_durum_comboBox.addItem("Aktif")
        self.k_durum_comboBox.addItem("Pasif")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 480, 81, 20))
        self.label_8.setObjectName("label_8")
        self.k_sifre_input = QtWidgets.QLineEdit(self.centralwidget)
        self.k_sifre_input.setGeometry(QtCore.QRect(540, 480, 171, 22))
        self.k_sifre_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.k_sifre_input.setObjectName("k_sifre_input")
        self.k_ekle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.k_ekle_btn.setGeometry(QtCore.QRect(540, 510, 93, 28))
        self.k_ekle_btn.setObjectName("k_ekle_btn")
        # kullanıcı ekle butonuna tıklayınca
        self.k_ekle_btn.clicked.connect(self.Kullanici_Ekle)
        ##########################################
        self.k_duzenle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.k_duzenle_btn.setGeometry(QtCore.QRect(430, 370, 111, 28))
        self.k_duzenle_btn.setObjectName("k_duzenle_btn")
        # kullanıcı duzenle butonuna tıklayınca
        self.secili_tablo=""
        self.k_duzenle_btn.clicked.connect(self.Kullanici_Duzenle)
        self.secili_tablo=""

        self.k_sil_btn=QtWidgets.QPushButton(self.centralwidget)
        self.k_sil_btn.setGeometry(QtCore.QRect(540, 370, 93, 28))
        self.k_sil_btn.setObjectName("k_sil_btn")
        # Kullanıcı sil butonuna tıklayınca
        self.k_sil_btn.clicked.connect(self.Kullanici_Sil)



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anasayfa"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>IP Listesi</p></body></html>"))
        self.ip_duzenle_btn.setText(_translate("MainWindow", "Seçili IP Duzenle"))
        self.label_2.setText(_translate("MainWindow", "Admin"))
        self.label_3.setText(_translate("MainWindow", "IP Adres"))
        self.baslat_btn.setText(_translate("MainWindow", "Başlat"))
        self.durdur_btn.setText(_translate("MainWindow", "Durdur"))
        self.label_5.setText(_translate("MainWindow", "IP Adresi"))
        self.label_6.setText(_translate("MainWindow", "IP Adı"))
        self.ip_ekle_btn.setText(_translate("MainWindow", "IP Ekle"))

        self.ip_sil_btn.setText(_translate("MainWindow", "Seçili IP Sil"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Kullanıcı Listesi</span></p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)



        self.label_7.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.label_9.setText(_translate("MainWindow", "Durumu"))
        self.label_8.setText(_translate("MainWindow", "Kullanıcı Şifre"))
        self.k_ekle_btn.setText(_translate("MainWindow", "Kullanıcı Ekle"))
        self.k_duzenle_btn.setText(_translate("MainWindow", "Kullanıcı Düzenle"))
        self.k_sil_btn.setText(_translate("MainWindow", "Kullanıcı Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

