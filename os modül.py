import os


for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("D:/"):


    print("Şu anki dizin",klasör_yolu)
    print("Klasörler ",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")