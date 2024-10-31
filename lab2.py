# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Input tipe tiket
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()

# Input status member
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Menentukan harga tiket berdasarkan tipe tiket dan member
if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

# Menghitung harga dengan diskon jika pengguna adalah member
if status_member == "ya":
    total_harga = harga_tiket * 0.8  # Diskon 20%
else:
    total_harga = harga_tiket

# Output total harga yang harus dibayar
print("Total harga yang harus dibayar: Rp", int(total_harga))
