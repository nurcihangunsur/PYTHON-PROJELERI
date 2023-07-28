print("Lunapark hız trenine hoş geldiniz..")
 
boy = int(input('Boyunuzun uzunluğunu "santimetre" cinsinden giriniz...\n'))
 
if boy >= 120:
  print("Hız trenine binebilirsiniz...")
 
  yas = int(input("Bilet parası için kaç yaşında olduğunuzu söyler misiniz?\n"))  
 
  if yas < 12:
    print("Bilent ücretiniz: 15 TL")
  elif yas <= 18:
    print ("Bilent ücretiniz: 25 TL")
  else:
    print("Bilet ücretiniz: 35 TL")
    
else:
  print("Üzgünüz, hız trenine binme koşulunu sağlamıyorsunuz...")