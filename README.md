# Lab_UAS_Prog

Program ini adalah aplikasi sederhana untuk mengelola daftar buku. Pengguna dapat:

1. Menambahkan buku ke dalam daftar.
2. Melihat daftar buku yang ada.
3. Menghapus buku dari daftar.
4. Menambahkan beberapa buku dalam satu sesi.

Struktur Program

Program ini terdiri dari beberapa file Python yang masing-masing memiliki tanggung jawab tertentu. Berikut adalah struktur file dan penjelasan masing-masing komponen:

1. data.py: Kelas Data untuk mengelola data buku.
2. view.py: Kelas View untuk menangani interaksi dengan pengguna.
3. process.py: Kelas Process untuk menghubungkan antara Data dan View, serta mengelola logika program.
4. main.py: File utama untuk menjalankan aplikasi.

# Penjelasan Kode

1. Class Data (data.py)
  - __init__: Konstruktor yang diinisialisasi saat objek Data dibuat. Di sini, kita membuat atribut books yang merupakan list kosong untuk menyimpan judul buku.
  - add_book(title): Metode untuk menambahkan judul buku ke dalam list books.
  - remove_book(title): Metode untuk menghapus judul buku dari list books jika judul tersebut ada.
  - get_books(): Metode untuk mengembalikan daftar buku yang ada.
    
2. Class View (view.py)
   - display_books(books): Metode untuk menampilkan daftar buku. Jika daftar kosong, akan menampilkan pesan bahwa daftar buku kosong.
   - get_user_input(): Metode untuk meminta input dari pengguna, yaitu judul buku yang ingin ditambahkan.
   - show_message(message): Metode untuk menampilkan pesan kepada pengguna, seperti konfirmasi setelah menambahkan atau menghapus buku.

3. Class Process (process.py)
   - __init__: Konstruktor yang menginisialisasi objek Data dan View.
   - add_book(): Metode untuk menambahkan buku. Menggunakan loop untuk memungkinkan pengguna menambahkan beberapa buku dalam satu sesi. Setelah menambahkan buku, program 
   - menanyakan apakah pengguna ingin menambah buku lagi.
   - remove_book(): Metode untuk menghapus buku dengan meminta input dari pengguna.
   - show_books(): Metode untuk menampilkan daftar buku yang ada.
   - run(): Metode utama yang menjalankan program. Menampilkan menu dan menangani pilihan pengguna untuk menambah, menghapus, atau menampilkan buku, serta keluar dari program.

4. File Utama (main.py)
   - File ini adalah titik masuk untuk menjalankan aplikasi. Ketika file ini dijalankan, objek Process dibuat dan metode run() dipanggil untuk memulai interaksi dengan pengguna.

# Cara Menjalankan Program

1. Pastikan semua file (data.py, view.py, process.py, dan main.py) berada dalam satu direktori.
2. Jalankan main.py menggunakan Python.
3. Ikuti instruksi di menu untuk menambah, menghapus, atau menampilkan daftar buku.

Dokumentasi Pembuatan & Menjalankan Program : 
https://youtu.be/5Ct_Xhct8UQ
