
# Class Nilai
class Nilai:
    def __init__(self, kode_mk, skor):
        self.kode_mk = kode_mk
        self.skor = skor


# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


# Class Mata Kuliah
class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama


# Class Program Studi
class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk):
        self.daftar_matakuliah.append(mk)


# Class Universitas
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# Membuat Universitas
uni = Universitas("Universitas A")

# Membuat 3 Program Studi
ti = uni.buat_program("Teknik Informatika")
si = uni.buat_program("Sistem Informasi")
mi = uni.buat_program("Manajemen Informatika")

# Membuat Mata Kuliah
ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

si.tambah_matakuliah(MataKuliah("SI101", "Analisis Sistem"))
si.tambah_matakuliah(MataKuliah("SI102", "Basis Data"))

mi.tambah_matakuliah(MataKuliah("MI101", "Manajemen Umum"))
mi.tambah_matakuliah(MataKuliah("MI102", "Administrasi Bisnis"))

# Membuat 3 Mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Menambahkan nilai mahasiswa
m1.tambah_nilai(Nilai("TI101", 85))
m1.tambah_nilai(Nilai("TI102", 90))

m2.tambah_nilai(Nilai("SI101", 80))
m2.tambah_nilai(Nilai("SI102", 90))

m3.tambah_nilai(Nilai("MI101", 75))
m3.tambah_nilai(Nilai("MI102", 85))

semua_mahasiswa = [m1, m2, m3]

# Menampilkan daftar Program Studi dan Mata Kuliah
print("DAFTAR PROGRAM STUDI")

for prodi in uni.programs:
    print("\nProgram Studi:", prodi.nama)
    for mk in prodi.daftar_matakuliah:
        print("-", mk.kode, mk.nama)

# Menampilkan nilai mahasiswa
print("\nDAFTAR NILAI MAHASISWA")

for m in semua_mahasiswa:
    print("\nNIM:", m.nim)
    print("Nama:", m.nama)

    for n in m.daftar_nilai:
        print(n.kode_mk, ":", n.skor)

    print("Rata-rata:", round(m.rata_rata(), 2))


# Fungsi laporan Program Studi
def report_program(prodi, semua_mahasiswa):
    print("\nLAPORAN PROGRAM STUDI:", prodi.nama)

    kode_mk = [mk.kode for mk in prodi.daftar_matakuliah]
    print("Mata Kuliah:", ", ".join(kode_mk))

    print("Mahasiswa dan rata-rata nilai:")

    for m in semua_mahasiswa:
        relevan = [
            n for n in m.daftar_nilai
            if n.kode_mk in kode_mk
        ]

        if relevan:
            rata = sum(n.skor for n in relevan) / len(relevan)
            print(m.nim, "-", m.nama, ":", round(rata, 2))


# Memanggil laporan setiap Program Studi
for prodi in uni.programs:
    report_program(prodi, semua_mahasiswa)
