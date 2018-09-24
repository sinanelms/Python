import sqlite3

import time

class Darkorbit():

    def __init__(self,tarih,tp,seref,rutbe,uridium):

        self.tarih = tarih
        self.tp = tp
        self.seref = seref
        self.rutbe = rutbe
        self.uridium = uridium

    def __str__(self):

        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.tarih,self.tp,self.seref,self.rutbe,self.uridium)


class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists darkorbit (tarih TEXT,tp INT,seref INT,rutbe INT,uridium INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitapları_goster(self):

        sorgu =  "Select * From darkorbit"

        self.cursor.execute(sorgu)

        darkorbit = self.cursor.fetchall()

        if (len(darkorbit) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in darkorbit:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From darkorbit where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        darkorbit = self.cursor.fetchall()

        if (len(darkorbit) == 0):
            print("Böyle bir kitap bulunmuyor.....")
        else:
            kitap = Darkorbit(darkorbit[0][0],darkorbit[0][1],darkorbit[0][2],darkorbit[0][3],darkorbit[0][4])

            print(darkorbit)
    def kitap_ekle(self,darkorbit):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(darkorbit.isim,darkorbit.yazar,darkorbit.yayınevi,darkorbit.tür,darkorbit.baskı))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From darkorbit where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

