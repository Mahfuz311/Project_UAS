# view.py
class View:
    @staticmethod
    def display_menu():
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Keluar")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def show_error(message):
        print(f"Error: {message}")

    @staticmethod
    def show_table(data):
        if not data:
            print("Tidak ada data untuk ditampilkan.")
            return

        print("\nData:")
        print("+----------------+-----+")
        print("| Nama           | Umur|")
        print("+----------------+-----+")
        for record in data:
            print(f"| {record['name']:<14} | {record['age']:<3} |")
        print("+----------------+-----+")
