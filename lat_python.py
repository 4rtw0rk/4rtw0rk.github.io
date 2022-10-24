xorang = int(input("Masukkan Angkanya : "))
if xorang in range(100, 900):
    print("Angkanmu Besar")
elif xorang in range (1000, 5000):
    print(">>", xorang, ": Angkamu Besar Sekali")
elif xorang < 100:
    print(">>", xorang,": Angkamu Kecil")
else:
    print("Salah Input. Ulangi")
