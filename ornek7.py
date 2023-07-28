"""10-20 arası sayılardan oluşan sayilar isimli bir liste oluşturun. 
Oluşturulan liste ile sayilar2=[21,22,23,24,25] listesini birleştirerek 4’e tam bölünen sayıları 
ekrana yazdırınız."""

sayilar = [10,11,12,13,14,15,16,17,18,19,20]
sayilar2 = [21,22,23,24,25]
sayilarYeni = sayilar + sayilar2

for i in sayilarYeni:
    if i%4==0:
        print(i)