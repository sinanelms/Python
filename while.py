print("""Her bir while döngüsünde kullanıcıdan bir sayı alın
 ve kullanıcının girdiği sayıları "toplam" isimli bir 
 değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü
  sonlandırın ve ekrana "toplam değişkenini" bastırın.""")

liste =[]
while True:
    a= input("bir sayı giriniz: ")
    if a =="q":
        break
    else:
        liste.append(a)
        print(liste)

