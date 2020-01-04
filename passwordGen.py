import random

lChars = 'abcçdefgğhiıjklmnoöpqrsştuüvwxyz'
uChars = 'ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ'
digits = '1234567890'
specialChars = '!@#$%^&*-_+='

passLen = 10  # çıktı bunun bir fazlası olacak
myPass = ""

for i in range(passLen):
    while (len(myPass)) <= 2:
        index = random.randrange(len(lChars))
        myPass = myPass + lChars[index]
        myPassLen = len(myPass)
    while (len(myPass)) <= 5:
        index = random.randrange(len(digits))
        myPass = myPass + digits[index]
        myPassLen = len(myPass)
    while (len(myPass)) <= 7:
        index = random.randrange(len(specialChars))
        myPass = myPass + specialChars[index]
        myPassLen = len(myPass)
    while (len(myPass)) <= 10:
        index = random.randrange(len(uChars))
        myPass = myPass + uChars[index]
        myPassLen = len(myPass)

print("Oluşturulun random şifresi: "+ myPass)