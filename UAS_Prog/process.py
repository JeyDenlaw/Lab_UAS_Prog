from data import Data
from view import View

class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def add_book(self):
        while True:
            title = self.view.get_user_input()
            self.data.add_book(title)
            self.view.show_message(f"Buku '{title}' telah ditambahkan.")
            
            another = input("Apakah Anda ingin menambah buku lagi? (y/n): ").strip().lower()
            if another != 'y':
                break

    def remove_book(self):
        title = self.view.get_user_input()
        self.data.remove_book(title)
        self.view.show_message(f"Buku '{title}' telah dihapus.")

    def show_books(self):
        books = self.data.get_books()
        self.view.display_books(books)

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Buku")
            print("2. Hapus Buku")
            print("3. Tampilkan Daftar Buku")
            print("4. Keluar")
            choice = input("Pilih opsi: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.show_books()
            elif choice == '4':
                print("Keluar dari program.")
                break
            else:
                print("Opsi tidak valid. Silakan coba lagi.")