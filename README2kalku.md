## Program Kalkulator Sederhana
Program ini adalah kalkulator sederhana yang memungkinkan pengguna untuk melakukan operasi aritmatika dasar: penjumlahan, pengurangan, perkalian, dan pembagian. Program ini ditulis dalam Python dan menggunakan input dari pengguna untuk mendapatkan angka dan jenis operasi yang diinginkan.

## Deskripsi Program
program ini dibuat menggunakan bahasa python dengan fitur :

Memungkinkan pengguna untuk memasukkan dua angka.
Mendukung empat operasi aritmatika:
Penjumlahan (+)
Pengurangan (-)
Perkalian (*)
Pembagian (/)
Menangani pembagian dengan nol dengan pesan kesalahan yang sesuai.
Menawarkan opsi untuk melakukan perhitungan baru setelah hasil ditampilkan.

## Flowchart Program
![Flowchart](https://github.com/fitrirmdhni22/lab2py/blob/main/flowchartkalku.drawio.png?raw=true)

## Kode Program
```python
# Program Kalkulator Sederhana

# Meminta pengguna memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Meminta pengguna memilih operator
print("Pilih operasi aritmatika:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
operator = input("Masukkan pilihan operasi (+, -, *, /): ")

# Menggunakan if, elif, else untuk menentukan operasi yang sesuai
if operator == '+':
    hasil = angka1 + angka2
    print("Hasil dari penjumlahan:", hasil)
elif operator == '-':
    hasil = angka1 - angka2
    print("Hasil dari pengurangan:", hasil)
elif operator == '*':
    hasil = angka1 * angka2
    print("Hasil dari perkalian:", hasil)
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil dari pembagian:", hasil)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operator tidak valid. Silakan pilih (+, -, *, /).")
```
## Output Program
```
PS C:\Users\AXIOO\Documents\laporan praktikum 3> & C:/Users/AXIOO/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/AXIOO/Documents/laporan praktikum 3/lab2 kasus 2.py"
Masukkan angka pertama: 20
Masukkan angka kedua: 30
Pilih operasi aritmatika:
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
Masukkan pilihan operasi (+, -, *, /): +
Hasil dari penjumlahan: 50.0
```
## Cara Kerja
Pengguna memasukkan 20 dan 30.
Pengguna memilih operator +.
Program menghitung 20 + 30 dan menampilkan hasil 50.0.
Program menanyakan apakah pengguna ingin melakukan perhitungan lagi.
Jika pengguna memilih 'y', proses dimulai lagi; jika 'n', program berhenti.
