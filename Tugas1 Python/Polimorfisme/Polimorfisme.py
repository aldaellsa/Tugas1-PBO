
from multipledispatch import dispatch
class BangunDatar(object):

  @dispatch(int)
  def luas(sisi):
    print("Luas Persegi: ", sisi * sisi)

  @dispatch(int)
  def keliling(sisi):
    print("Keliling Persegi: ", 4 * sisi)

  @dispatch(float)
  def luas(r):
    print("Luas Lingkaran: ", 3.14 * r ** 2)

  @dispatch(float)
  def keliling(r):
    print("Keliling Lingkaran: ", 2 * 3.14 * r)

  @dispatch(int,int)
  def luas(panjang, lebar):
    print("Luas Persegi Panjang: ", panjang * lebar)

  @dispatch(int,int)
  def keliling(panjang, lebar):
    print("Keliling Persegi Panjang: ", 2 * panjang + 2 * lebar)

  @dispatch(int,int)
  def luas(alas, tinggi):
    print("Luas Segitiga: ",  alas * tinggi * 1/2)

  
    
class Main():
  
  def menu():
    print("\n\nPolimorfisme Program")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Persegi Panjang")
    print("4. Segitiga")

  menu()
  pilihan = int(input("\nPilih Menu: "))

  while pilihan != 5:
    if pilihan == 1:
     persegi = BangunDatar()
     print("Menghitung Luas dan Keliling Persegi")
     sisi = int(input("Masukkan Sisi: ")) 
     persegi.luas(sisi)
     persegi.keliling(sisi)
     break
    
    elif pilihan == 2:
     lingkaran = BangunDatar()
     print("Menghitung Luas dan Keliling Lingkaran")
     r = int(input("Masukkan Jari-jari: "))
     lingkaran.luas(r)
     lingkaran.keliling(r)
     break

    elif pilihan == 3:
     persegiPanjang = BangunDatar()
     print("Menghitung Luas dan Keliling Persegi Panjang")
     panjang = int(input("Masukkan Panjang: "))
     lebar = int(input("Masukkan Lebar: "))
     persegiPanjang.luas(panjang, lebar)
     persegiPanjang.keliling(panjang, lebar)
     break
    
    elif pilihan == 4:
     segitiga = BangunDatar()
     print("Menghitung Luas Segitiga")
     alas = int(input("Masukkan Alas: "))
     tinggi = int(input("Masukkan Tinggi: "))
     segitiga.luas(alas, tinggi)
     break
