import sqlite3
con = sqlite3.connect("dersler.db")
cursor = con.cursor()


def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad Text,numara INT,ogrencinotu INT)")
    
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES(' Nurcihan ', 'Gunsur',1234,89)")
    con.commit()
    con.close()

tabloolustur()
degerekle()

