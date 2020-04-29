from collections import Counter
import re

class LogParser:
    def __init__(self, log_name):
        self.log_name = log_name

    def get_most_common(self, top):
        self.top = top
        with open(self.log_name, "r") as read_log:
            ip_count = Counter(line.split()[0] for line in read_log.readlines() if not line.isspace()).most_common(top)
        return ip_count

    def log_by_http_code(self, output_file, code):
        self.output_file = output_file
        self.code = code
        pattern = re.compile(r'\s[\d]{3}\s')
        with open(self.log_name, 'r') as read_log:
            with open(self.output_file, 'w') as write_log:
                for line in read_log.readlines():
                    match = pattern.search(line)
                    if match == self.code:
                        write_log.write(line)
