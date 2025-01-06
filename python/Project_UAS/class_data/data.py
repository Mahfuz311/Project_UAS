# data.py
class Data:
    def __init__(self):
        self.records = []

    def add_record(self, name, age):
        self.records.append({"name": name, "age": age})

    def get_all_records(self):
        return self.records
