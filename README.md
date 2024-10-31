# Program Harga Tiket
Program ini adalah program harga tiket yang menghitung total biaya tiket
berdasarkan dua faktor utama: tipe tiket (Reguler atau VIP) dan status keanggotaan (apakah pengguna memiliki kartu member atau tidak)

# Program ini dibuat menggunakan bahasa python dengan fitur:
1. Input dan Output: input(): Untuk menerima masukan dari pengguna. print(): Untuk menampilkan output ke konsol.
2. Tipe Data: String: Menyimpan tipe tiket dan status member sebagai teks. Integer: Menggunakan harga tiket sebagai angka.
3. Pengkondisian: if, elif, dan else: Untuk menentukan harga tiket berdasarkan input pengguna dan memberikan diskon jika pengguna adalah anggota.
4. Operasi Aritmetika: Menghitung total harga dengan mengalikan harga tiket dan mengurangi 20% jika pengguna memiliki kartu member.
5. Fungsi lower(): Untuk mengubah input menjadi huruf kecil, sehingga memudahkan validasi.
6. Penggunaan List: Menggunakan in untuk memeriksa validitas tipe tiket dalam list yang berisi "reguler" dan "vip".

# Flowchart Program
![Flowchart](https://github.com/fitrirmdhni22/lab2.py/blob/main/flowchartdiskon.drawio.png?raw=true)

# Kode Program Tiket
``` python
# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Input tipe tiket
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
```    
# Output Program Tiket
````
PS C:\Users\AXIOO\Documents\laporan praktikum 3> & C:/Users/AXIOO/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/AXIOO/Documents/laporan praktikum 3/lab2.py"
Masukkan tipe tiket (reguler/vip): reguler
Apakah Anda memiliki kartu member? (ya/tidak): ya
Total harga yang harus dibayar: Rp 40000
PS C:\Users\AXIOO\Documents\laporan praktikum 3> & C:/Users/AXIOO/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/AXIOO/Documents/laporan praktikum 3/lab2.py"
Masukkan tipe tiket (reguler/vip): vip
Apakah Anda memiliki kartu member? (ya/tidak): tidak
Total harga yang harus dibayar: Rp 100000
PS C:\Users\AXIOO\Documents\laporan praktikum 3> 
````
## Cara kerja 
Program mulai dengan meminta pengguna untuk memasukkan tipe tiket yang diinginkan (reguler atau VIP) menggunakan fungsi input(). Kemudian, program menanyakan apakah pengguna memiliki kartu member dengan pertanyaan lain. input yang diterima diubah menjadi huruf kecil dengan lower(), sehingga proses validasi menjadi lebih mudah dan tidak tergantung pada kapitalisasi. Program memeriksa apakah tipe tiket yang dimasukkan termasuk dalam daftar valid ("reguler" atau "vip"): Jika valid, program akan melanjutkan ke langkah berikutnya.Jika tidak valid, program akan menampilkan pesan kesalahan dan berhenti menggunakan exit(). Menentukan Harga Tiket Berdasarkan tipe tiket yang valid, program menetapkan harga: Jika "reguler", harga ditetapkan ke Rp 50.000. Jika "vip", harga ditetapkan ke Rp 100.000. Program memeriksa status keanggotaan: Jika pengguna memiliki kartu member ("ya"), program menghitung total harga dengan diskon 20%. Jika pengguna tidak memiliki kartu member ("tidak"), program menggunakan harga tiket penuh. Jika status member tidak valid, program akan menampilkan pesan kesalahan dan berhenti. Total harga dihitung berdasarkan harga tiket dan status member yang telah divalidasi. Program mencetak total harga yang harus dibayar oleh pengguna menggunakan print().C
