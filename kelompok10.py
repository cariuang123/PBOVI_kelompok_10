class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                 jenis_layanan_kereta, rute, jumlah_kursi, jenis_gerbong):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_layanan_kereta = jenis_layanan_kereta
        self.rute = rute
        self.jumlah_kursi = jumlah_kursi
        self.jenis_gerbong = jenis_gerbong

    def tambah_rute(self, new_rute):
        self.rute.append(new_rute)

    def kurangi_rute(self, old_rute):
        if old_rute in self.rute:
            self.rute.remove(old_rute)
    def info(self):
        return f"Kereta {self.nama} ({self.warna}) dengan rute {', '.join(self.rute)}\n" \
               f"Tahun Keluaran: {self.tahun_keluaran}, Kecepatan: {self.kecepatan}, Bahan Bakar: {self.bahan_bakar}, " \
               f"Jumlah Roda: {self.jumlah_roda}, Kapasitas Penumpang: {self.kapasitas_penumpang}, " \
               f"Jenis Layanan Kereta: {self.jenis_layanan_kereta}, Jumlah Kursi: {self.jumlah_kursi}, " \
               f"Jenis Gerbong: {self.jenis_gerbong}"
class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                 jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil
        self.engine_status = False

    def start_engine(self):
        self.engine_status = True
        print(f"Mesin {self.nama} dinyalakan.")

    def stop_engine(self):
        self.engine_status = False
        print(f"Mesin {self.nama} dimatikan.")

    def maju(self):
        if self.engine_status:
            print(f"{self.nama} sedang bergerak maju.")
        else:
            print(f"Untuk bergerak maju, nyalakan mesin terlebih dahulu.")

    def mundur(self):
        if self.engine_status:
            print(f"{self.nama} sedang bergerak mundur.")
        else:
            print(f"Untuk bergerak mundur, nyalakan mesin terlebih dahulu.")

    def belok(self, arah):
        if self.engine_status:
            print(f"{self.nama} sedang berbelok {arah}.")
        else:
            print(f"Untuk berbelok, nyalakan mesin terlebih dahulu.")

    def info(self):
        return f"{self.jenis_mobil} {self.nama} ({self.warna})\n" \
               f"Tahun Keluaran: {self.tahun_keluaran}, Kecepatan: {self.kecepatan}, Bahan Bakar: {self.bahan_bakar}, " \
               f"Jumlah Roda: {self.jumlah_roda}, Kapasitas Penumpang: {self.kapasitas_penumpang}, " \
               f"Engine Status: {'On' if self.engine_status else 'Off'}"


class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                 jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                         jenis_mobil)
        self.front_wing = front_wing
        self.rear_wing = rear_wing

    def race(self):
        if self.engine_status:
            print(f"{self.nama} sedang balapan dengan kecepatan {self.kecepatan} km/h.Dengan front wing:{self.front_wing} dan rear wing:{self.rear_wing} ")
        else:
            print(f"Untuk race, nyalakan mesin terlebih dahulu.")
        
    def info(self):
        return f"Mobil Balap {self.nama} ({self.warna})\n" \
               f"Tahun Keluaran: {self.tahun_keluaran}, Kecepatan: {self.kecepatan}, Bahan Bakar: {self.bahan_bakar}, " \
               f"Jumlah Roda: {self.jumlah_roda}, Kapasitas Penumpang: {self.kapasitas_penumpang}, " \
               f"Jenis Mobil: {self.jenis_mobil}, Front Wing: {self.front_wing}, Rear Wing: {self.rear_wing}"\
               f"Engine Status: {'On' if self.engine_status else 'Off'}"
class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                 jenis_mobil, sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, 
                         jenis_mobil)
        self.sunroof_type = sunroof_type
        self.shock_breaker = shock_breaker

    def sunroof_terbuka(self):
        if self.engine_status:
            print(f"{self.nama} sunroof terbuka .")
        else:
            print(f"Untuk membuka sunroof, nyalakan mesin terlebih dahulu.")
        

    def sunroof_tertutup(self):
        if self.engine_status:
            print(f"{self.nama} sunroof tertutup.")
        else:
            print(f"Untuk menutup sunroof, nyalakan mesin terlebih dahulu.")
        
    def info(self):
        return f"Mobil Crossroad {self.nama} ({self.warna})\n" \
               f"Tahun Keluaran: {self.tahun_keluaran}, Kecepatan: {self.kecepatan}, Bahan Bakar: {self.bahan_bakar}, " \
               f"Jumlah Roda: {self.jumlah_roda}, Kapasitas Penumpang: {self.kapasitas_penumpang}, " \
               f"Jenis Mobil: {self.jenis_mobil}, Sunroof Type: {self.sunroof_type}, " \
               f"Shock Breaker: {self.shock_breaker}"\
               f"Engine Status: {'On' if self.engine_status else 'Off'}"
def mobil():
    while True:
        print("=========Mobil=======")
        print("1. input informasi")
        print("2. start Engine")
        print("3. stop Engine")
        print("4. maju")
        print("5. mundur")
        print("6. belok")
        print("7. informasi")
        print("8. back")

        choice = input("Pilih menu (1-8): ")

        if choice == "1":
            tahun_keluaran = int(input("Masukkan tahun keluaran: "))
            nama = input("Masukkan nama: ")
            warna = input("Masukkan warna: ")
            kecepatan = int(input("Masukkan kecepatan: "))
            bahan_bakar = input("Masukkan bahan bakar: ")
            jumlah_roda = int(input("Masukkan jumlah roda: "))
            kapasitas_penumpang = int(input("Masukkan kapasitas penumpang: "))
            jenis_mobil = input("Masukkan jenis mobil: ")
            mobil = Mobil(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                                     jenis_mobil)

            print("Mobil Balap berhasil ditambahkan!")

        elif choice == "2":
            mobil.start_engine()
            
        elif choice == "3":
           mobil.stop_engine()
        
        elif choice == "4":
            mobil.maju()
        elif choice == "5":
            mobil.mundur()
        elif choice == "6":
            belok=input("masukan arah belokan:")
            mobil.belok(belok)
        elif choice == "7":
            print(mobil.info())
        elif choice == "8":
            main()

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
def kereta():
    while True:
        print("=========kereta=======")
        print("1. input informasi")
        print("2. hapus rute")
        print("3. Tambah rute")
        print("4. info kereta")
        print("5. back")

        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            tahun_keluaran = int(input("Masukkan tahun keluaran: "))
            nama = input("Masukkan nama: ")
            warna = input("Masukkan warna: ")
            kecepatan = int(input("Masukkan kecepatan: "))
            bahan_bakar = input("Masukkan bahan bakar: ")
            jumlah_roda = int(input("Masukkan jumlah roda: "))
            kapasitas_penumpang = int(input("Masukkan kapasitas penumpang: "))
            jenis_layanan_kereta = input("Masukkan jenis layanan kereta: ")
            rute = input("Masukkan rute (pisahkan dengan koma): ").split(", ")
            jumlah_kursi = int(input("Masukkan jumlah kursi: "))
            jenis_gerbong = input("Masukkan jenis gerbong: ")

            kereta = Kereta(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                            jenis_layanan_kereta, rute, jumlah_kursi, jenis_gerbong)

            print("Kereta berhasil ditambahkan!")

        elif choice == "2":
            del_rute = input("Masukkan rute baru (pisahkan dengan koma): ")
            kereta.kurangi_rute(del_rute)
            print(f"rute {del_rute} berhasil dihapus!")
        

        elif choice == "3":
           new_rute = input("Masukkan rute baru (pisahkan dengan koma): ")
           kereta.tambah_rute(new_rute)
           print(f"rute {new_rute} berhasil ditambahkan")
        
        elif choice == "4":
            print(kereta.info())
        elif choice == "5":
            main()

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
def mobil_balap():
    while True:
        print("=========Mobil Balap=======")
        print("1. input informasi")
        print("2. start Engine")
        print("3. stop Engine")
        print("4. maju")
        print("5. mundur")
        print("6. belok")
        print("7. race")
        print("8. informasi")
        print("9. back")

        choice = input("Pilih menu (1-9): ")

        if choice == "1":
            tahun_keluaran = int(input("Masukkan tahun keluaran: "))
            nama = input("Masukkan nama: ")
            warna = input("Masukkan warna: ")
            kecepatan = int(input("Masukkan kecepatan: "))
            bahan_bakar = input("Masukkan bahan bakar: ")
            jumlah_roda = int(input("Masukkan jumlah roda: "))
            kapasitas_penumpang = int(input("Masukkan kapasitas penumpang: "))
            jenis_mobil = input("Masukkan jenis mobil: ")
            front_wing = input("Masukkan jenis front wing: ")
            rear_wing = input("Masukkan jenis rear wing: ")

            mobil_balap = MobilBalap(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                                     jenis_mobil, front_wing, rear_wing)

            print("Mobil Balap berhasil ditambahkan!")
            print(mobil_balap.info())
        elif choice == "2":
            mobil_balap.start_engine()
            
        elif choice == "3":
           mobil_balap.stop_engine()
        
        elif choice == "4":
            mobil_balap.maju()
        elif choice == "5":
            mobil_balap.mundur()
        elif choice == "6":
            belok=input("masukan arah belokan:")
            mobil_balap.belok(belok)

        elif choice == "7":
            mobil_balap.race()

        elif choice == "8":
           print(mobil_balap.info())
        
        elif choice == "9":
            main()

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
def mobil_cross_road():
    while True:
        print("=========Mobil Cross Road=======")
        print("1. input informasi")
        print("2. start Engine")
        print("3. stop Engine")
        print("4. maju")
        print("5. mundur")
        print("6. belok")
        print("7. buka sunroof")
        print("8. tutup sunroof")
        print("9. informasi")
        print("10. back")

        choice = input("Pilih menu (1-10): ")

        if choice == "1":
            tahun_keluaran = int(input("Masukkan tahun keluaran: "))
            nama = input("Masukkan nama: ")
            warna = input("Masukkan warna: ")
            kecepatan = int(input("Masukkan kecepatan: "))
            bahan_bakar = input("Masukkan bahan bakar: ")
            jumlah_roda = int(input("Masukkan jumlah roda: "))
            kapasitas_penumpang = int(input("Masukkan kapasitas penumpang: "))
            jenis_mobil = input("Masukkan jenis mobil: ")
            sunroof_type = input("Masukkan jenis sunroof: ")
            shock_breaker = input("Masukkan jenis shock breaker: ")

            mobil_crossroad = MobilCrossroad(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda,
                                             kapasitas_penumpang, jenis_mobil, sunroof_type, shock_breaker)

            print("Mobil Crossroad berhasil ditambahkan!")
        elif choice == "2":
            mobil_crossroad.start_engine()
            
        elif choice == "3":
           mobil_crossroad.stop_engine()
        
        elif choice == "4":
            mobil_crossroad.maju()
        elif choice == "5":
            mobil_crossroad.mundur()
        elif choice == "6":
            belok=input("masukan arah belokan:")
            mobil_crossroad.belok(belok)

        elif choice == "7":
            mobil_crossroad.sunroof_terbuka()

        elif choice == "8":
            mobil_crossroad.sunroof_tertutup()
        
        elif choice == "9":
            print(mobil_crossroad.info())
            main()
        elif choice == "10":
            main()

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

def main():
    while True:
        print("Menu:")
        print("1. Tambah Kereta")
        print("2. Tambah Mobil")
        print("3. Tambah Mobil Balap")
        print("4. Tambah Mobil Crossroad")
        print("5. Keluar")

        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            kereta()

        elif choice == "2":
            mobil()

        elif choice == "3":
            mobil_balap()
        
        elif choice == "4":
            mobil_cross_road()
        elif choice == "5":
            print("Program selesai")
            break
        

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()

