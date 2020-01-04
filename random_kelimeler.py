# Harf tekrarlı 4-10 karakter uzunluğunda bütün kombinasyonlar
import itertools
listem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
kombinasyonlar = []
for uzunluk in range(4, 11):
    for kombinasyon in itertools.combinations_with_replacement(listem, uzunluk):
        kombinasyonlar.append("".join(kombinasyon))

# Harf tekrarsız 4-10 karakter uzunluğunda bütün kombinasyonlar
import itertools
listem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
kombinasyonlar = []
for uzunluk in range(4, 11):
    for kombinasyon in itertools.combinations(listem, uzunluk):
        kombinasyonlar.append("".join(kombinasyon))
print(kombinasyonlar)
print(len(kombinasyonlar))