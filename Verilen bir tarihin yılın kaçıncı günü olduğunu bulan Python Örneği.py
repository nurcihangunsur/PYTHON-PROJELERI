 
def ArtikYil(yil):
    artik=False
    if yil%400==0 or (yil%4==0 and yil%100!=0): artik=True
    return artik
 
def YilinGünü(Ay,Gün,Yil):
    gunler=[31,28,31,30,31,30,31,31,30,31,30,31]
    if ArtikYil(Yil):
        gunler[1]=29
    sira=0
    for a in range(Ay-1):
        sira+=gunler[a]
    sira+=Gün
    return sira
 
print(YilinGünü(4,9,2018))