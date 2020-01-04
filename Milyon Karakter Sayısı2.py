#girilen dosyada aynı karakterden kaç tane bulunduğunu hesaplar

import collections
import pprint

with open("kararlar.txt", 'r',encoding="utf-8") as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
    print(value)
    exit()






