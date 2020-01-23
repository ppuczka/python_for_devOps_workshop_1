from pprint import pprint
import re

with open("sample_log.log", 'r') as log_file:
    logs = log_file.readlines()

for log in logs:
    print(log)
    if log.__contains__("INFO") and re.search("\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", log):
       
        with open("filtered_logs_log", 'a') as filtered_log:
            filtered_log.write(log)
        