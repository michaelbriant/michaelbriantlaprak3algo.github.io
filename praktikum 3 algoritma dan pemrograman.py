print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

#  menginput angka awla dan angka akhir
angka_awal = int(input("Masukkan angka awal: "))
angka_akhir = int(input("Masukkan angka akhir: "))

# Memastikan angka awal lebih kecil dari angka akhir
if angka_awal > angka_akhir:
    angka_awal, angka_akhir = angka_akhir, angka_awal

# Menampilkan angka dengan urutan yang dimodifikasi menggunakan while
i = angka_awal
j = angka_akhir

while i < j:
    print(f"{i} | {j}")
    i += 1
    j -= 1



print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

# Menerima input total harga belanjaan
total_harga = float(input("Masukkan total harga belanjaan: Rp. "))

# Menerima input jumlah uang dari pelanggan
jumlah_uang = float(input("Masukkan jumlah uang yang diberikan: Rp. "))

# Menghitung kembalian
kembalian = jumlah_uang - total_harga

# Inisialisasi daftar lembar uang dengan nilai nominal
lembar_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Inisialisasi daftar jumlah lembar uang yang dibutuhkan
jumlah_lembar_uang = [0, 0, 0, 0, 0, 0, 0]

# Menghitung jumlah lembar uang yang dibutuhkan
for i in range(len(lembar_uang)):
    if kembalian >= lembar_uang[i]:
        jumlah_lembar_uang[i] = int(kembalian / lembar_uang[i])
        kembalian = kembalian % lembar_uang[i]

# Menampilkan kembalian
print("Kembalian: Rp", round(jumlah_uang - total_harga, 2))

# Menampilkan jumlah lembar uang yang dibutuhkan
for i in range(len(lembar_uang)):
    if jumlah_lembar_uang[i] > 0:
        print("Lembar", lembar_uang[i], ":", jumlah_lembar_uang[i], "lembar")
