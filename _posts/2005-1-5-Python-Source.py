print("---------------------------------------------------")
print("Variabel")
print("---------------------------------------------------")

a = 10
b = 2
xdata = 20

print()
print("---------------------------------------------------")
print("Output dan Tipe Data (Casting)")
print("---------------------------------------------------")

x_integer = int(xdata)
x_float = float(xdata)
x_boolean = bool(xdata)
x_string = str(xdata)
print(x_integer, "adalah type data : ", type(x_integer))
print(x_float, "adalah type data : ", type(x_float))
print(x_boolean, "adalah type data : ", type(x_boolean))
print(x_string, "adalah type data : ", type(x_string)) 

print()
print("---------------------------------------------------")
print("Indexing dan Slicing")
print("---------------------------------------------------")

xsaya   = "Muhammad Aditya"
print("Inisial Saya :", xsaya[0], xsaya[9] )
print("Panggilan Saya :", xsaya[9:15])

print()
print("---------------------------------------------------")
print("Input dan List")
print("---------------------------------------------------")

xbulan = "Januari","Februari","Maret"
print("Bulan ",xbulan[1])
xnama = input("Nama : ")
print(">> Hai", xnama,"di Bulan" ,xbulan[1],
    "\n>> Semoga Cerah dan Tetap Semangat")

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
