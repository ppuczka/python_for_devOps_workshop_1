import datetime

class ConverterHistory():
    
    def __init__(self, history_file_path):
        self.history_file_path = history_file_path

    # @staticmethod
    def append_to_history(self, write_content):
        date_time_curent = datetime.datetime.now()
        
        history_file = open(self.history_file_path, "a")
        history_file.write(str(date_time_curent) + write_content)
        print(write_content)
        