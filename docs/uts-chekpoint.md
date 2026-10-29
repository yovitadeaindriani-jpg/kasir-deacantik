Week 08 - UTS Project Checkpoint
1. Requirement Coverage with Evidence
Project Simple Cashier telah menggabungkan materi Minggu 01-07 sebagai checkpoint sebelum melanjutkan ke Minggu 09.

Minggu 01 - Repository dan Git: Project dikelola menggunakan Git dengan branch untuk pengerjaan setiap minggu.
Minggu 02-03 - Class, Object, dan Encapsulation: Class Product digunakan untuk mengelola produk, harga, stok, dan subtotal. Harga tidak dapat diubah langsung melalui property read-only, sedangkan perubahan harga dan stok divalidasi melalui method.
Minggu 04 - Inheritance dan Polymorphism: FoodProduct dan DigitalProduct menjadi variasi produk. Method get_description() digunakan untuk menampilkan deskripsi produk.
Minggu 05 - List dan Dictionary: ProductCatalog digunakan untuk mengelola koleksi produk, mencari produk berdasarkan kode, dan melakukan pencarian nama produk.
Minggu 06 - Stack dan Queue: ActionHistory digunakan untuk demonstrasi Stack dengan prinsip LIFO, sedangkan OrderQueue digunakan untuk demonstrasi Queue dengan prinsip FIFO.
Minggu 07 - File Handling dan Persistence: ProductRepository membaca dan menyimpan data produk melalui CSV, sedangkan OrderRepository membaca dan menyimpan data pesanan melalui JSON.
Bukti pengujian awal tersedia melalui output python main.py, yang menampilkan demonstrasi materi Minggu 02-07 dan alur transaksi sederhana.

2. Findings and Actions
Temuan selama checkpoint:

Program dapat dijalankan menggunakan python main.py.
Validasi harga dan stok berjalan sesuai hasil pengujian.
Katalog dapat menampilkan produk serta melakukan pencarian nama tanpa membedakan huruf besar dan kecil.
Queue memproses elemen dengan prinsip FIFO, sedangkan Stack menggunakan prinsip LIFO.
Perubahan stok produk dapat disimpan ke CSV dan dibaca kembali.
Data produk dan pesanan yang berubah akibat pengujian dipulihkan menggunakan Git agar tidak ikut terbawa sebagai perubahan checkpoint.
Tindakan yang dilakukan adalah menyusun ulang main.py menjadi demonstrasi materi sebelumnya, memperbarui .gitignore, dan menyiapkan dokumentasi checkpoint.

3. Layer Boundary Check
Pembagian tanggung jawab project:

Models: Mengelola objek produk, variasi produk, dan katalog.
Services: Menangani struktur data dan riwayat aksi.
Repositories: Menangani proses membaca dan menyimpan data ke file.
main.py: Menjalankan demonstrasi materi dan menghubungkan komponen yang digunakan.
Akses file CSV dan JSON seharusnya ditangani oleh repository, bukan dilakukan langsung oleh model atau service. Pemeriksaan batas tanggung jawab antarlapisan perlu dilakukan sebelum checkpoint dinyatakan selesai.

4. Demo Scenario
Skenario demonstrasi checkpoint:

Membuat objek Product dan menghitung subtotal untuk dua unit produk.
Menguji penolakan perubahan langsung pada property harga.
Menguji validasi harga negatif dan pengurangan stok yang melebihi persediaan.
Menampilkan variasi Product, FoodProduct, dan DigitalProduct.
Memuat data produk dari data/products.csv.
Menampilkan katalog dan menguji pencarian produk.
Membandingkan perilaku Queue FIFO dan Stack LIFO.
Membaca stok awal produk Indomie.
Menjalankan transaksi penjualan tiga unit jika stok mencukupi, lalu menyimpan perubahan ke file.
Membaca ulang data untuk memeriksa stok dan jumlah pesanan yang tersimpan.
Pada pengujian dengan data awal yang berisi empat produk dan stok Indomie sebanyak 20 unit, stok menjadi 17 setelah penjualan tiga unit.

5. Chain Explanation
Alur konsep project:

Class -> Object -> Data Structure -> Repository -> File

Class: Menentukan atribut dan perilaku objek.
Object: Merupakan instance dari class, misalnya produk Indomie.
Data Structure: Menyimpan dan mengelola kumpulan data, misalnya List, Dictionary, Stack, dan Queue.
Repository: Menangani proses penyimpanan dan pembacaan data.
File: Menyimpan data agar tetap tersedia setelah program berhenti.
Pada Minggu 09, bagian penyimpanan direncanakan beralih dari file menuju database sesuai materi berikutnya.

6. State Carried into Week 09
Kondisi yang dibawa ke Minggu 09:

Materi dasar Minggu 01-07 telah dirangkum dalam demonstrasi checkpoint.
Data produk disimpan melalui CSV dan data pesanan melalui JSON.
Pemisahan tanggung jawab antara model, service, repository, dan main.py perlu tetap dipertahankan.
Pengembangan berikutnya mengikuti modul Minggu 09, terutama perubahan mekanisme penyimpanan dari file ke database.
Tidak ada fitur baru yang ditambahkan di luar kebutuhan checkpoint ini.