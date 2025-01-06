# main.py
from class_data.data import Data
from class_view.view import View
from class_process.process import Process

data = Data()
view = View()
process = Process(data, view)

while True:
    view.display_menu()
    choice = view.get_input("Pilih menu: ")

    if choice == "1":
        process.add_data()
    elif choice == "2":
        process.show_data()
    elif choice == "3":
        print("Keluar dari program.")
        break
    else:
        view.show_error("Pilihan tidak valid.")
