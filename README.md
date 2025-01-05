# DAFTAR ISI

- [PROJECT UAS](#project-uas)
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



### STEP 2: CLASS VIEW
#### CLASS VIEW
Bertugas untuk menangani semua interaksi dengan pengguna, termasuk menampilkan menu, menerima input, dan menampilkan data dalam bentuk tabel.

* Komponen Utama:
  * ```display_menu()```: Menampilkan menu pilihan.
  * ```get_input(prompt)```: Menerima input dari pengguna.
  * ```show_error(message)```: Menampilkan pesan error.
  * ```show_table(data)```: Menampilkan data dalam format tabel.
* Keunggulan: Memisahkan logika antarmuka dengan logika data dan proses.



### STEP 3: CLASS PROCESS
#### CLASS PROCES
Menghubungkan Data dan View. Bertanggung jawab untuk memproses logika program, validasi input, dan melakukan operasi utama seperti menambah atau menampilkan data.

* Komponen Utama:
  * ```add_data()```: Meminta input, memvalidasi, dan menyimpan data.
  * ```show_data()```: Mengambil data dari Data dan menampilkan melalui View.
* Keunggulan: Kelas ini bertindak sebagai penghubung antara antarmuka pengguna dan logika penyimpanan data.



#### Alur Program main
File utama yang mengintegrasikan modul data, view, dan process.

* Integrasi Modul:
  * Data, View, dan Process diimport dan dihubungkan.
  * Process mengelola alur proses berdasarkan input dari pengguna.



### RUNNING PROGRAM
Langkah terakhir yaitu pengujian code program,
# KESIMPULAN

