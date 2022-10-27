import datetime as dt
# # #  --- 01 / 02 --- # # #
print()
print("%"*60)
print(" 01 General, Variabel, Input, Output, Tipe Data Casting")
print(" 02 Operasi Penugasan, Aritmatika, Perbandingan, Logika")
print("%"*60)
# --- Tr 01/02 ---
print(" 01a variabel, \\, \\t, \\n, \\b")
print(" 01b input(), print(), type() ")
print(" 01c int(), float(), bool(), str()")
print(" 02a Op. Penugasan \t\t=, +=, -=, *=, /=, **=, %=")
print(" 02b Op. Aritmatika \t+, -, *, /, %")
print(" 02c Op. Perbandingan \t<, >, >=, <=, ==, !=")
print(" 02d Op. Logika \t\tnot, or, and xor")
# --- Pr 01 ---
print("="*60)
a = 10
b = 4
c = True
d = False
t_text = "\tis type\t"
print(" 01a Variabel \ta =", a)
print(" 01a Variabel \tb =", b)
print(" 01b Masukkan Input Type Data : 45")
xdata = 45
x_float = float(xdata)
x_boolean = bool(xdata)
print(" 01c TD. Casting \tfloat() =>", x_float, t_text, type(x_float))
print(" 01c TD. Casting \tbool() =>", x_boolean, "\t", t_text, type(x_boolean))
# --- Pr 02 ---
print("-"*60)
xassign = a = b
xkali = a * b
xprioritas = a + b * a
xhasil2 = a == b
xhasil3 = c and d
print(" 02a Op. Penugasan \t\ta = b\t\t=", xassign)
print(" 02b Op. Aritmatika \ta * b\t\t=", xkali)
print(" 02x Op. Prioritas \t\ta + b * a   =", xprioritas)
print(" 02c Op. Perbandingan \ta == b\t\t=", xhasil2)
print(" 02d Op. Logika \t\tc dan d\t\t=", xhasil3)
print()

# # #  --- 03 / 04 --- # # #
print("%"*60)
print(" 03 Indexing, Slicing dan List")
print(" 04 Hitung, Minimum, Maxsimum, Method, Uppercase, Lowercase")
print("%"*60)
# --- Tr 03 / 04 ---
print(" 03a Indexing \t\t\t\txvar[xindex]")
print(" 03b Slincing \t\t\t\txvar[xslincing]")
print(" 03c List \t\t\t\t\txvar[xlist]")
print(" 04a Hitung \t\t\t\tlen(xvar)")
print(" 04b Minimal & Maximal \t\tmin(), max()")
print(" 04c Method \t\t\t\txvar.count()")
print(" 04d Uppercase & Lowercase \tx.upper(), xlower()")
print("-"*60)
# --- Pr 03 ---
xsaya = "Muhammad", "Aditya"
xbulan = "Januari", "Februari", "Maret"
h = "Saya Adalah Pahlawan Super"
xinisial1 = xsaya[0]
xinisial2 = xsaya[1]
print(" 03a Indexing \t\tInisial Saya \t:", xinisial1[0], xinisial2[0])
print(" 03b Slincing \t\tPanggilan Saya \t:", xinisial2)
print(" 03c list \t\t\tBulan \t\t\t:", xbulan[1])
# --- Pr 04 ---
xhitung = len(h)
xh_huruf = h.count("a")
xmin = min(h)
xmax = max(h)
xedit = xsaya[1]
xupper = xedit.upper()
xlower = xedit.lower()
print(" 04a Hitung Kotak \t\t:", xhitung)
print(" 04b Min & Max Var \t\t:", xmin, "&", xmax)
print(" 04c Method Huruf a \t:", xh_huruf)
print(" 04d Uppercase & Lowercase \t:", xupper, xlower)

# # #  --- 05 / 06 --- # # #
print("%"*60)
print(" 05 Format String")
print(" 06 Date Time")
print("%"*60)
# --- Tr 05 / 06 ---
print(' 05 Format String \tf"{xvar:xordo}xstr" :+, :1% :, :. :.3f :>4')
print(" 06 dt.date.today()")
# --- Pr 05 --
print("-"*60)
xdepan = "Aditya"
xsaku = 5000000
xlengkap = f"{xdepan}, punya uang Rp {xsaku:,}"
print(" 05a Format \t\t", xlengkap)
# --- 06 ---
xday = dt.date.today()
xtahun = int(input(" 05b ITahun \t\t: "))
xbulan = int(input("     IBulan \t\t: "))
xtanggal = int(input("     ITanggal \t\t: "))
xttl = dt.date(xtahun, xbulan, xtanggal)
xtotalday = (xday - xttl)
xtotaltahun = xtotalday / 365
# xsisabulan = xtotalday - (xtotaltahun.days * 365)
# sisa_bulan = (xday - xttl) - int(xxumur * 365)
print(f"     Hari ini \t\t: {xday}, {xday:%A}")
print(f"     Tanggal Lahir \t: {xttl}, {xttl:%A}")
print(f"     Umurku \t\t: {xtotaltahun.days} Tahun")
print()

# # #  --- 07 / 08 --- # # #
print("%"*60)
print(" 07 Abc")
print(" 08 Abc")
print("%"*60)
# --- Pr 05 --
print("-"*60)

"""
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
"""