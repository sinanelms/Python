

def ortalamabul(sayilar):
    toplam =0
    for sayi in sayilar:
        toplam += sayi
    print("Genel Ortalama",toplam/len(sayilar))

ortalamabul(range(5))