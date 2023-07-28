# Kullanıcının girdiği sayının rakamlarını toplayan python örneği
sayi=input("Bir sayı girin: ")#str formatında giriş yapar
toplam=0
for rakam in sayi:
  toplam += int(rakam)
 
print("sayının rakamları toplamı:",toplam)