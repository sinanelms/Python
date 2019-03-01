from random import random
import time


while True:
    sans = int(input("Deneme sayısı: "))
    for k in range(sans):
        a = int(random() * 10)
        b = int(random() * 10)
        c = int(random() * 10)
        time.sleep(0.5)

        if a==b==c:
            print(k + 1, ". deneme: ", a, b, c, "Üçlü tamamlandı")
            break
        elif a==b or a==c or b==c:
            print(k + 1, ". deneme: ", a, b, c, "İkili tamamlandı")
        else:
            print(k + 1, ". deneme: ", a, b, c)
