# process.py
class Process:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_data(self):
        try:
            name = self.view.get_input("Masukkan nama: ").strip()
            if not name:
                raise ValueError("Nama tidak boleh kosong.")

            age = self.view.get_input("Masukkan umur: ").strip()
            if not age.isdigit():
                raise ValueError("Umur harus berupa angka.")

            self.data.add_record(name, int(age))
            print("Data berhasil ditambahkan!")
        except ValueError as e:
            self.view.show_error(e)

    def show_data(self):
        records = self.data.get_all_records()
        self.view.show_table(records)
