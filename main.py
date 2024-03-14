import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sefere_uzunlugu = int(input("Şifre uzunluğu girin \n"))

sefere = ""

for i in range(sefere_uzunlugu):
    sefere += random.choice(karakterler)

print(sefere)