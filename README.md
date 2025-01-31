# DAFTAR ISI

- [PROJECT UAS](#project-uas)
  - [CODE PROGRAM PENGELOLAAN DATA SEDERHANA](code-program-pengelolaan-data-sederhana)
  - [KESIMPULAN](#kesimpulan)
  - [LINK YOUTUBE](#link-youtube)

# PROJECT UAS
## CODE PROGRAM PENGELOLAAN DATA SEDERHANA
### STEP 1: CLASS DATA
#### CLASS DATA
Bertanggung jawab untuk mengelola data, seperti menyimpan dan mengambil data.
* Komponen Utama:
  * ```add_record(name, age)```: Menambahkan data ke dalam daftar.
  * ```get_all_records()```: Mengambil semua data untuk ditampilkan.
* Keuntungan: Kelas ini dapat diperluas untuk mendukung berbagai operasi data tanpa mengubah modul lain.

<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/Class_Data.png">

### STEP 2: CLASS VIEW
#### CLASS VIEW
Bertugas untuk menangani semua interaksi dengan pengguna, termasuk menampilkan menu, menerima input, dan menampilkan data dalam bentuk tabel.

* Komponen Utama:
  * ```display_menu()```: Menampilkan menu pilihan.
  * ```get_input(prompt)```: Menerima input dari pengguna.
  * ```show_error(message)```: Menampilkan pesan error.
  * ```show_table(data)```: Menampilkan data dalam format tabel.
* Keunggulan: Memisahkan logika antarmuka dengan logika data dan proses.

<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/Class_View.png">

### STEP 3: CLASS PROCESS
#### CLASS PROCES
Menghubungkan Data dan View. Bertanggung jawab untuk memproses logika program, validasi input, dan melakukan operasi utama seperti menambah atau menampilkan data.

* Komponen Utama:
  * ```add_data()```: Meminta input, memvalidasi, dan menyimpan data.
  * ```show_data()```: Mengambil data dari Data dan menampilkan melalui View.
* Keunggulan: Kelas ini bertindak sebagai penghubung antara antarmuka pengguna dan logika penyimpanan data.

<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/Class_Process.png">

#### Alur Program main
File utama yang mengintegrasikan modul data, view, dan process.

* Integrasi Modul:
  * Data, View, dan Process diimport dan dihubungkan.
  * Process mengelola alur proses berdasarkan input dari pengguna.

<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/main.png">

### RUNNING PROGRAM
Langkah terakhir yaitu pengujian code program

Di sini saya tidak memasukan no 1, 2, 3, maka hasilnya ```error:```
<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/run_error.png">


* Menambahkan Data dengan menginputkan N0 1 dan menginputkan Usia
<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/tambah_data.png">



* Menginputkan angka 2 untuk menampilkan data yang sudah kita tambahkan sebelumnya
<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/tampilkan_data.png">



* Dan yang terakhir menginputkan angka 3 untuk keluar dari program
<img src="https://github.com/Mahfuz311/Project_UAS/blob/main/python/ss/keluar.png">

## KESIMPULAN
Program ini mencerminkan implementasi OOP dan modularitas dengan desain yang bersih.

Cocok untuk proyek kecil hingga besar, dengan fleksibilitas tinggi untuk pengembangan lebih lanjut.

## LINK YOUTUBE
https://youtu.be/PIF6M8JZ164
