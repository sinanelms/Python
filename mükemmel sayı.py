print("""
***************************************************
***************************************************
**   Bir sayının kendi hariç bölenlerinin toplamı**
**kendine eşitse bu sayıya "mükemmel sayı" denir.** 
**Örnek olarak, 6 mükemmel bir sayıdır.          **
**(1 + 2 + 3 = 6)                                **
*************************************************
*************************************************
""")
liste =[]

while True:
    a=int(input("Bir sayı giriniz: "))

    for i in range(1,a):
        if (a%i==0):
            liste.append(i)

            for i in liste:
                i+=i
    print(i+1)
    break





