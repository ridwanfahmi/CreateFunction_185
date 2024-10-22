import math #library untuk operasi matematika

#Fungsi lambda digunakan untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r
#lambda r: merupakan cara singkat mendefinisikan fungsi anonim yang menerima satu argumen, yaitu jari-jari (r)

#Contoh penggunaan fungsi luas_lingkaran
jari_jari = 7
#Menghitung luas lingkaran dengan jari-jari 7
area = luas_lingkaran(jari_jari)

#{area: 2f} digunakan untuk membatasi dua angka di belakang koma pada hasil luas lingkaran
print(f"Luas Lingkaran dengan jari - jari {jari_jari} adalah {area:.2f}")
