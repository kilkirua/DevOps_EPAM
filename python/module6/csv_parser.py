import csv

class CsvParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def sell_over(self, item_type, threshold):
        self.item_type = str(item_type)
        self.threshold = int(threshold)
        with open(self.file_name, 'r') as f_read:
            csv_reader = csv.DictReader(f_read)
            country_list = []
            for line in csv_reader:
                if line["Item Type"] == self.item_type and float(line["Units Sold"]) > self.threshold:
                    country_list.append(line["Country"])
        return sorted(country_list)

    def get_country_profit(self, country):
        self.country = country
        with open(self.file_name, 'r') as f_read:
            reader = csv.DictReader(f_read)
            total_profit = 0
            for line in reader:
                if line["Country"] == self.country:
                    total_profit = total_profit + float(line["Total Profit"])
            return round(total_profit, 2)

    def save_as(self, new_file_name, delimiter):
        self.new_file_name = new_file_name
        self.delimiter = delimiter
        with open(self.file_name, 'r') as f_read:
            with open(self.new_file_name, 'w') as f_write:
                reader = csv.reader(f_read)
                writer = csv.writer(f_write, delimiter=self.delimiter)
                for line in reader:
                    writer.writerow(line)