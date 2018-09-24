print("""*********************
ATM Makinesine HOŞGELDİNİZ

İşlemler;

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan çıkmak için "q"ya basın
*********************




""")

bakiye =1000

while True:
    islem = input("İşlemi Giriniz: ")

    if (islem == "q"):
        print("Yine Bekleriz")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Miktarı giriniz: "))

        bakiye +=miktar

    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz: "))

        if (bakiye - miktar <0):
            print("Bu miktarda para çekemezsiniz")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz İşlem....")

