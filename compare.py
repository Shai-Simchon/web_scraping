import csv
import datetime

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def compare_csv(current_csv, previous_csv):
    new_data = []
    for row in current_csv:
        if row not in previous_csv:
            new_data.append(row)
    return new_data

def sort_csv_by_column(csv_data, column_index):
    # Sort the CSV data by the specified column index
    sorted_data = sorted(csv_data, key=lambda x: int(x[column_index - 1]))  # Adjust index to start from 0
    return sorted_data

def filter_rows_by_value(csv_data, column_index, max_value):
    # Filter rows where the value in the specified column is less than or equal to max_value
    filtered_data = [row for row in csv_data if int(row[column_index - 1]) <= max_value]  # Adjust index to start from 0
    return filtered_data

def main():
    # Assuming your CSV files are named with the date, e.g., "2024-05-12.csv"
    today = datetime.date.today()
    current_file_path = f"{today}.csv"
    
    # Get the date of the previous day
    yesterday = today - datetime.timedelta(days=1)
    previous_file_path = f"{yesterday}.csv"
    
    try:
        current_csv = read_csv(current_file_path)
        previous_csv = read_csv(previous_file_path)
        
        new_data = compare_csv(current_csv, previous_csv)
        
        if new_data:
            print("New data found:")
            # Filter rows where the value in column 1 is less than or equal to 100
            filtered_new_data = filter_rows_by_value(new_data, column_index=4, max_value=100)
            for row in filtered_new_data:
                print(row)
        else:
            print("No new data found.")
    
    except FileNotFoundError:
        print("One of the files not found. Could be the first day of logging.")

if __name__ == "__main__":
    main()
