vize = int(input("Vize notunuzu giriniz!"))
proje  = int(input("Proje notunuzu giriniz!"))
final = int(input("Final notunuzu giriniz!"))
 
ortalama = vize * 0.3 + proje * 0.3 + final * 0.4
print ("Not ortalaması: ", ortalama)
 
if(ortalama >= 90):
  print("Harf Notu: AA")
elif(ortalama >= 85):
  print("Harf Notu: BA")
elif(ortalama >= 80):
  print("Harf Notu: BB")
elif(ortalama >= 75):
  print("Harf Notu: CB")
elif(ortalama >= 70):
  print("Harf Notu: CC")
elif(ortalama >= 65):
  print("Harf Notu: DC")
elif(ortalama >= 60):
  print("Harf Notu: DD")
elif(ortalama >= 50):
  print("Harf Notu: FD")
else:
  print("Harf Notu: FF")