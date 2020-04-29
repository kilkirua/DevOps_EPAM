from collections import Counter

class LogParser:
    def __init__(self, log_name):
        self.log_name = log_name

    def get_most_common(self, top):
        self.top = top
        with open(self.log_name, "r") as read_log:
            ip_count = Counter(i.split()[0] for i in read_log.readlines() if len(i) > 1).most_common(top)
        return ip_count

    def log_by_http_code(self, output_file, code):
        self.output_file = output_file
        self.code = code
        with open(self.log_name, 'r') as read_log:
            with open(self.output_file, 'w') as write_log:
                for i in read_log.readlines():
                    if len(i) > 1 and i.split()[8] == self.code:
                        write_log.write(i)