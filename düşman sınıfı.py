import random
import time
class Dusman:


    def __init__(self, isim,kalan_can,saldiri_gucu,mermi_sayisi):
        self.isim = isim
        self.kalan_can =kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + "saldırıyor..")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " kadar mermi harcandı")
        self.mermi_sayisi -= harcanan_mermi

        return (harcanan_mermi,self.saldiri_gucu)
    def saldiriyauğra(self,harcanan_mermi, saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= harcanan_mermi*saldiri_gucu
    def mermi_bitti_mi(self):
        if self.mermi_sayisi <= 0 :
            print(self.isim + "Konuşuyor : Mermi bitti. Oyundan çıkıyorum")
            return True
        return False
    def hayatta_mi(self):
        if (self.kalan_can <=0):
            print("Ölüyorummmmmmm...")






    def print(self):
        print("Başlıyor......")
        print("isim:",self.isim,"Kalan Can:",self.kalan_can,"Saldırı Gücü:",self.saldiri_gucu,"Mermi Sayısı: ",self.mermi_sayisi)

dusmanlar = []
i = 0
while (i <10):
    rastgelecan =random.randrange(100,200)
    rastgelesaldirigucu =random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i +=1

for dusman in dusmanlar:
    dusman.print()


i =0
while (i<3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0, 10)
    donendeger = dusmanlar[randomdusman1].saldir()
    dusmanlar[randomdusman2].saldiriyauğra(donendeger[0],donendeger[1])
    time.sleep(3)
    print("Raund Bitti")

    i +=1