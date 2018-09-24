def tambölenleribulma(sayı):
    tambölen=[]
    for i in range(2,sayı):
        if (sayı %i==0):
            tambölen.append(i)
    return tambölen
while True:
    sayı =input("sayı: ")

    if (sayı =="q"):
        print("sonlandırılıyor")
        break
    else:
        sayı =int(sayı)
        print("tambölenler",tambölenleribulma(sayı))
