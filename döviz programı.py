import requests

url ="http://api.fixer.io/latest?base="


birinci_doviz = input("Birinci Döviz: ")
ikinci_doviz = input("İkinici Döviz: ")
miktar = float(input("Miktarı giriniz: "))

response=requests.get(url+birinci_doviz)
json_verisi = response.json()
try:
    print(float(veri["rates"][ikinci_doviz]) * miktar)
except KeyError:
    print("Lütfen para birimlerini kontrol edin")