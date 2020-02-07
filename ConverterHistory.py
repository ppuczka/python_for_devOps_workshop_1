import datetime

class ConverterHistory():
    
    def __init__(self, history_file_path):
        self.history_file_path = history_file_path

    
    def append_to_history(self, write_contentA, write_contentB, convert_from, convert_to):
        date_time_curent = datetime.datetime.now()
        current_date_formatted = date_time_curent.strftime("%d-%m-%Y %H:%M:%S")
        
        history_file = open(self.history_file_path, "a")
        history_file.write(f"""Date: {str(current_date_formatted)}:
            user entered value: {write_contentA} {convert_from}  
            converted to: {convert_to}
            result: {write_contentB} \n""")
        