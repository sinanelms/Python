toplam = 0
a,b =0,1
while(True):
    a,b = b, a+b
    if a> 4000000:
        break
    else:
        if a%2 == 0:
            toplam += a
print(toplam)