class View:
    def display_books(self, books):
        if not books:
            print("Daftar buku kosong.")
        else:
            print("Daftar Buku:")
            for book in books:
                print(f"- {book}")

    def get_user_input(self):
        return input("Masukkan judul buku: ")

    def show_message(self, message):
        print(message)