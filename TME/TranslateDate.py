from datetime import datetime

def convert_date():
    date_input = input("Enter the date (mm/dd/yyyy): ")
    date_obj = datetime.strptime(date_input, "%m/%d/%Y")
    print("Date Output:", date_obj.strftime("%B %d, %Y"))

convert_date()