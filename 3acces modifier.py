
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim
        self.nama = nama
        self._semester = semester
        self.__ipk = ipk

    # Getter semester
    def get_semester(self):
        return self._semester

    # Setter semester
    def set_semester(self, semester_baru):
        if semester_baru < 1:
            raise ValueError("Semester tidak valid")
        self._semester = semester_baru

    # Getter IPK
    def get_ipk(self):
        return self.__ipk

    # Setter IPK
    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0")
        self.__ipk = ipk_baru

    def tampilkan_data(self):
        print("NIM:", self.nim)
        print("Nama:", self.nama)
        print("Semester:", self.get_semester())
        print("IPK:", self.get_ipk())


# Membuat 2 objek mahasiswa
m1 = Mahasiswa("202512029", "Nia", 3, 3.75)
m2 = Mahasiswa("202512030", "Alya", 3, 3.50)

print("DATA MAHASISWA AWAL")

m1.tampilkan_data()
print()
m2.tampilkan_data()

# Mengubah semester dan IPK
m1.set_semester(4)
m1.set_ipk(3.90)

m2.set_semester(4)
m2.set_ipk(3.80)

print("\nDATA MAHASISWA SETELAH DIUBAH")

m1.tampilkan_data()
print()
m2.tampilkan_data()
