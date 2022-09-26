class BangunDatar:
    def luas(self):
        print("Menghitung Luas Bangun Datar")
    def keliling(self):
        print("Menghitung Keliling Bangun Datar")

class Persegi(BangunDatar):
    def sisi(self):
        pass

class PersegiPanjang(BangunDatar):
    def panjang(self):
        pass
    def lebar(self):
        pass

class Segitiga(BangunDatar):
    def alas(self):
        pass
    def tinggi(self):
        pass

class Lingkaran(BangunDatar):
    def r(self):
        pass

class Main():
  
  def menu():
    ProgramHitung = BangunDatar()
    ProgramHitung.luas()
    ProgramHitung.keliling()
    print("\n\nInheritance Program")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Persegi Panjang")
    print("4. Segitiga")
    

  menu()
  pilihan = int(input("\nPilih Menu: "))

  while pilihan != 5:
    if pilihan == 1:
     persegi = Persegi()
     print("Menghitung Luas dan Keliling Persegi")
     persegi.sisi = int(input("Masukkan Sisi: ")) 
     persegi.luas()
     persegi.keliling()
     break
    
    elif pilihan == 2:
     lingkaran = Lingkaran()
     print("Menghitung Luas dan Keliling Lingkaran")
     lingkaran.r = int(input("Masukkan Jari-jari: "))
     lingkaran.luas()
     lingkaran.keliling()
     break

    elif pilihan == 3:
     persegiPanjang = PersegiPanjang()
     print("Menghitung Luas dan Keliling Persegi Panjang")
     persegiPanjang.panjang = int(input("Masukkan Panjang: "))
     persegiPanjang.lebar = int(input("Masukkan Lebar: "))
     persegiPanjang.luas()
     persegiPanjang.keliling()
     break

    
    elif pilihan == 4:
     segitiga = Segitiga()
     print("Menghitung Luas Segitiga")
     segitiga.alas = int(input("Masukkan Alas: "))
     segitiga.tinggi = int(input("Masukkan Tinggi: "))
     segitiga.luas()
     break
