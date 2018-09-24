#İlk yüz doğal sayının
# karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.
def karebul(x):
    liste=[]
    for i in range(1,(x+1)):
        a =i**2
        liste.append(a)
    return sum(liste)

def topkare(y):
    liste=[]
    for i in range (1,(y+1)):
        liste.append(i)
    return sum(liste)**2    

print(topkare(100) - karebul(100))