# Variabel
a = 10
b = 2
xdata = 20

# Tipe Data Casting
x_integer = int(xdata)
x_float = float(xdata)
x_boolean = bool(xdata)
x_string = str(xdata)
print(x_integer, "adalah type data : ", type(x_integer))
print(x_float, "adalah type data : ", type(x_float))
print(x_boolean, "adalah type data : ", type(x_boolean))
print(x_string, "adalah type data : ", type(x_string)) 

import os
os.system('cls')
os.system('clear')

xsaya   = "Muhammad Aditya"
print("Inisial Saya :", xsaya[0], xsaya[9] )

print("Panggilan Saya :", xsaya[9:15])


xbulan = "Januari","Februari","Maret"
print("Pendaftaran Bulan",xbulan[1])
xnama = input("Nama : ")
xumur = input("Umur : ")
xkota = input("Kota : ")
print(">> Pendaftaran Di bulan" ,xbulan[1],
    "\n>> Nama ", xnama,", Umur", xumur, "Tahun , Asal Kota", xkota,
    "\n>> Berhasil dibuat. Terima Kasih")

xorang = int(input("Masukkan Angkanya : "))
if xorang in range(100, 900):
    print("Angkanmu Besar")
elif xorang in range (1000, 5000):
    print(">>", xorang, ": Angkamu Besar Sekali")
elif xorang < 100:
    print(">>", xorang,": Angkamu Kecil")
else:
    print("Salah Input. Ulangi")


xwarna = "Pink", "Hitam", "Cokelat"
for xdaftar in range(len(xwarna)):
    print("Saya Tidak Suka Warna", xwarna[xdaftar])
