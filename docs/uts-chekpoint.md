Week 08 - UTS Project Checkpoint
1. Requirement Coverage with Evidence

Di checkpoint ini, saya merangkum semua materi Minggu 01-07 yang sudah diterapkan di project Simple Cashier, sebelum lanjut ke Minggu 09.

Minggu 01 - Repository dan Git: Project saya kelola dengan Git, dan setiap minggu dikerjakan di branch tersendiri.
Minggu 02-03 - Class, Object, dan Encapsulation: Class Product saya pakai untuk mengatur produk, harga, stok, dan subtotal. Harga tidak bisa diubah langsung karena dibuat sebagai property read-only. Untuk mengubah harga dan stok, harus lewat method yang sudah ada validasinya.
Minggu 04 - Inheritance dan Polymorphism: FoodProduct dan DigitalProduct adalah turunan dari produk dasar. Keduanya menampilkan deskripsi lewat method get_description().
Minggu 05 - List dan Dictionary: ProductCatalog dipakai untuk menyimpan kumpulan produk, mencari produk lewat kode, dan mencari produk lewat nama.
Minggu 06 - Stack dan Queue: ActionHistory menunjukkan cara kerja Stack (LIFO), sedangkan OrderQueue menunjukkan cara kerja Queue (FIFO).
Minggu 07 - File Handling dan Persistence: ProductRepository membaca dan menyimpan data produk ke CSV, sedangkan OrderRepository melakukan hal yang sama untuk data pesanan dalam format JSON.

Bukti pengujian awal bisa dilihat dari output python main.py, yang menampilkan demo materi Minggu 02-07 beserta alur transaksi sederhana.

2. Findings and Actions

Temuan selama checkpoint:

Program bisa dijalankan dengan python main.py.
Validasi harga dan stok berjalan sesuai hasil pengujian.
Katalog bisa menampilkan produk dan mencari nama produk tanpa peduli huruf besar atau kecil.
Queue memproses data secara FIFO, sedangkan Stack secara LIFO.
Perubahan stok bisa disimpan ke CSV dan terbaca lagi dengan benar.
Data produk dan pesanan yang berubah akibat pengujian saya kembalikan lewat Git, supaya tidak ikut tercatat sebagai perubahan checkpoint.

Tindakan yang saya lakukan: menyusun ulang main.py menjadi demo materi-materi sebelumnya, memperbarui .gitignore, dan menyiapkan dokumentasi checkpoint.

3. Layer Boundary Check

Pembagian tanggung jawab di project ini:

Models: mengurus objek produk, variasi produk, dan katalog.
Services: mengurus struktur data dan riwayat aksi.
Repositories: mengurus pembacaan dan penyimpanan data ke file.
main.py: menjalankan demo dan menghubungkan semua komponen.

Akses ke file CSV dan JSON seharusnya hanya dilakukan oleh repository, bukan langsung oleh model atau service. Batas tanggung jawab antarlapisan ini perlu saya cek lagi sebelum checkpoint dianggap selesai.

4. Demo Scenario

Skenario demo untuk checkpoint ini:

Membuat objek Product, lalu menghitung subtotal untuk dua unit.
Mencoba mengubah property harga secara langsung, dan memastikan perubahannya ditolak.
Menguji validasi harga negatif dan pengurangan stok yang melebihi persediaan.
Menampilkan variasi Product, FoodProduct, dan DigitalProduct.
Memuat data produk dari data/products.csv.
Menampilkan katalog dan mencoba pencarian produk.
Membandingkan perilaku Queue (FIFO) dengan Stack (LIFO).
Membaca stok awal produk Indomie.
Menjalankan transaksi penjualan tiga unit kalau stoknya cukup, lalu menyimpan perubahannya ke file.
Membaca ulang data untuk mengecek stok dan jumlah pesanan yang tersimpan.

Pada pengujian dengan data awal berisi empat produk dan stok Indomie 20 unit, stok berkurang menjadi 17 setelah penjualan tiga unit.

5. Chain Explanation

Alur konsep project ini:

Class → Object → Data Structure → Repository → File

Class: menentukan atribut dan perilaku sebuah objek.
Object: instance dari class, contohnya produk Indomie.
Data Structure: tempat menyimpan dan mengelola kumpulan data, seperti List, Dictionary, Stack, dan Queue.
Repository: bagian yang mengurus penyimpanan dan pembacaan data.
File: tempat data disimpan supaya tetap ada setelah program berhenti.

Di Minggu 09, penyimpanan rencananya akan dipindah dari file ke database, sesuai materi berikutnya.

6. State Carried into Week 09

Kondisi project yang dibawa ke Minggu 09:

Materi dasar Minggu 01-07 sudah dirangkum dalam demo checkpoint.
Data produk masih disimpan lewat CSV, dan data pesanan lewat JSON.
Pemisahan tanggung jawab antara model, service, repository, dan main.py harus tetap dijaga.
Pengembangan selanjutnya mengikuti modul Minggu 09, terutama perpindahan penyimpanan dari file ke database.
Tidak ada fitur baru yang ditambahkan di luar kebutuhan checkpoint ini.