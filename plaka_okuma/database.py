import sqlite3
def baglan(baglan):
    baglan= sqlite3.connect("veritabanı.db")

def admin():
    baglan(baglan)
    baglan.execute("CREATE TABLE ADMIN(ID TEXT NOT NULL,ADMIN_ADI TEXT,ADMIN_SIFRE TEXT)")
    baglan.execute("INSERT INTO ADMIN VALUES(?,?,?,?)",('1','engin','123456'))
    baglan.commit()
    result= baglan.execute("SELECT * FROM ADMIN")
    for data in result:
        print("ID :",data[0])
        print("EMAİL :",data[1])
        print("SIFRE :",data[2])
    baglan.close()
#admin()
def kullanıcı():
    baglan= sqlite3.connect("veritabanı.db")
    a="engin"
    b="123"
    c="1"
   # cursor tablodaki satır sayısı
    cursor = baglan.cursor()
    cursor.execute('SELECT COUNT(*) FROM KULLANICILAR')
    rowcount =str(cursor.fetchone()[0])
   ################
    baglan.execute("INSERT INTO KULLANICILAR VALUES(?,?,?,?)",(rowcount,a,b,c))
    baglan.commit()
    baglan.close()

def tablo_listeleme():
    baglan = sqlite3.connect("veritabanı.db")
    sorgu = baglan.execute("SELECT * FROM KULLANICILAR")
    vericek = sorgu.fetchall()  # felchall veri okuma toplu olarak okur
    for veri in vericek:
        print(veri[0],veri[1],veri[2],veri[3])
    baglan.commit()
    baglan.close()
tablo_listeleme()