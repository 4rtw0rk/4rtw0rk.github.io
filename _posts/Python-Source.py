print()
print("---------------------------------------------------")
print("# Variabel, Input, Output dan Tipe Data (Casting)")
print("---------------------------------------------------")

t_data = " => adalah type data => "
xdata = input("Masukkan Input Type Data : ")
x_integer = int(xdata)
x_float = float(xdata)
x_boolean = bool(xdata)
x_string = str(xdata)
print(x_integer, t_data, type(x_integer))
print(x_float, t_data, type(x_float))
print(x_boolean, t_data, type(x_boolean))
print(x_string, t_data, type(x_string))

print()
print("---------------------------------------------------")
print("# Operasi Aritmatika dan Komparasi")
print("---------------------------------------------------")

a = 10
b = 4
xtambah = a + b
xkurang = a - b
xkali = a * b
xbagi = a / b
xeksponen = a ** b
xmodulus = a % b
xfloordivision = a // b
xprioritas = a + b * a
print(xtambah, ",", xkurang, ",", xkali, ",", xbagi, ",", xeksponen, ",", xmodulus, ",", xfloordivision, ",", xprioritas)
xhasil1 = a > b
xhasil2 = a == b
print(xhasil1, ",", xhasil2)

print()
print("---------------------------------------------------")
print("Indexing, Slicing dan List")
print("---------------------------------------------------")

xsaya   = "Muhammad Aditya"
xbulan = "Januari","Februari","Maret"
print(">> Bulan", xbulan[1], "<<")
print("* Inisial Saya :", xsaya[0], xsaya[9], "\n* Panggilan Saya :", xsaya[9:15])
print(">> Semoga Sehat dan Tetap Semangat")

print()
print("---------------------------------------------------")
print("Percabangan")
print("---------------------------------------------------")
xorang = int(input("Masukkan Angkanya : "))
if xorang in range(100, 900):
    print("Angkanmu Besar")
elif xorang in range (1000, 5000):
    print(">>", xorang, ": Angkamu Besar Sekali")
elif xorang < 100:
    print(">>", xorang,": Angkamu Kecil")
else:
    print("Salah Input. Ulangi")

print()
print("---------------------------------------------------")
print("Perulangan")
print("---------------------------------------------------")

xwarna = "Pink", "Hitam", "Cokelat"
for xdaftar in range(len(xwarna)):
    print("Saya Tidak Suka Warna", xwarna[xdaftar])