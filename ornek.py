"""Kullanıcıya sinema ya da tiyatro tercihi sorulsun. 
Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. 
Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; 
öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız."""
secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci misiniz(E/H) : ")
ucret = 0
 
#indirimsiz ücret hesaplama
if secim == '1':
  ucret = 15 #sinema
elif secim == '2':
  ucret = 10 #tiyatro
 
#öğrenci indirimi
if ogrenci =='E' or ogrenci =='e':
  ucret=ucret / 2  #%50
 
print("Ödemeniz gereken ücret :{}".format(ucret))

