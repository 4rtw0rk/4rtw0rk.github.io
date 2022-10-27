# --- Title ---
print()
print("%"*60)
print(" 01 General, Variabel, Input, Output, Tipe Data Casting")
print(" 02 Operasi Penugasan, Aritmatika, Perbandingan, Logika")
print("%"*60)
# --- Teori ---
print(" 01a \\, \\t, \\n, \\b")
print(" 01b input(), print(), type() ")
print(" 01c int(), float(), bool(), str()")
print(" 02a Op. Penugasan \t\t=, +=, -=, *=, /=, **=, %=")
print(" 02b Op. Aritmatika \t+, -, *, /, %")
print(" 02c Op. Perbandingan \t<, >, >=, <=, ==, !=")
print(" 02d Op. Logika \t\tnot, or, and xor")
# --- Pr 01 ---
print("="*60)
t_text = "\tis type\t"
xdata = input(" 01b Masukkan Input Type Data : ")
x_integer = int(xdata)
x_float = float(xdata)
x_boolean = bool(xdata)
x_string = str(xdata)
print(" 01c int()\t =>", x_integer, "\t", t_text, type(x_integer))
print(" 01c float() =>", x_float, t_text, type(x_float))
print(" 01c bool()\t =>", x_boolean, t_text, type(x_boolean),
      "\n", "01c str()\t =>", x_string, "\t", t_text, type(x_string))
# --- Pr 02 ---
a = 10
b = 4
c = True
d = False
xtambah = " " + str(a + b)
xkurang = a - b
xkali = a * b
xbagi = a / b
xeksponen = a ** b
xmodulus = a % b
xfloordivision = a // b
xprioritas = a + b * a

print("-"*60)
print(xtambah, ",", xkurang, ",", xkali, ",", xbagi, ",", xeksponen,
      ",", xmodulus, ",", xfloordivision, ",", xprioritas)
xhasil1 = " " + str(a > b)
xhasil2 = a == b
xhasil3 = c and d
print(xhasil1, xhasil2, xhasil3)
# KE 03
print()
print("="*60)
print("03 Indexing, Slicing dan List")
print("="*60)
print("xvar[xindex], xvar[xslincing], xvar[xlist]")
print("-"*60)
xsaya = "Muhammad Aditya"
xbulan = "Januari", "Februari", "Maret"
print(">> Bulan", xbulan[1], "<<")
print("* Inisial Saya :", xsaya[0], xsaya[9])
print("* Panggilan Saya :", xsaya[9:15])
print(">> Semoga Sehat dan Tetap Semangat")
# KE 04
print()
print("="*60)
print("04 Hitung, Minimum, Maxsimum, Uppercase, Lowercase dan Method")
print("="*60)
print("len(xvar)")
print("xvar.count(), ")
print("-"*60)
h = "Saya Adalah Pahlawan Super"
xhitung = len(h)
xh_huruf = h.count("a")
xmin = min(h)
xmax = max(h)
print("Panjang Huruf :", xhitung)
print("Banyak Huruf a :", xh_huruf)
print("Minimum Variabel :", xmin)
# KE 05
print()
print("="*60)
print("05 Percabangan")
print("="*60)
xorang = int(input("Masukkan Angkanya : "))
if xorang in range(100, 900):
    print("Angkanmu Besar")
elif xorang in range(1000, 5000):
    print(">>", xorang, ": Angkamu Besar Sekali")
elif xorang < 100:
    print(">>", xorang, ": Angkamu Kecil")
else:
    print("Salah Input. Ulangi")
# KE 06
print()
print("="*60)
print("06 Perulangan")
print("="*60)
xwarna = "Pink", "Hitam", "Cokelat"
for xdaftar in range(len(xwarna)):
    print("Saya Tidak Suka Warna", xwarna[xdaftar])
