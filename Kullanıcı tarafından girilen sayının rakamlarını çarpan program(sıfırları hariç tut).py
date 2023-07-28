sayi=input("Bir sayı girin: ")#str formatında giriş yapar
carpim=1
for rakam in sayi:
  if int(rakam) != 0:
    carpim *= int(rakam)
 
print("sayının rakamları çarpımı:",carpim)