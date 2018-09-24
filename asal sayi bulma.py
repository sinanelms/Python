#problem 3
a = int(input("sayı: "))
def bul(sayı):
    if sayı % 2 ==0:
        return False
    for i in range(3,sayı,1):
        if sayı % i == 0:
            return False
    return True

liste=[]
for i in range(2,a):
    if a%i ==0 and bul(i)==True:
         liste.append(i)
         print(liste)

print(max(liste))