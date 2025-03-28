import os
import csv

def load_currency_data():
    file_path = os.path.join(os.path.dirname(__file__), 'currency.csv')

    data = {}
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            reader = csv.reader(file)
            next(reader, None)
            for rows in reader:
                try:
                    currency = rows[0].strip().upper()
                    rate = float(rows[2].strip())
                    data[currency] = rate
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data

def convert_currency():
    data = load_currency_data()

    if not data:
        print("Currency data could not be loaded. Exiting...")
        return

    try:
        amount = float(input("How much dollar do you have? "))
        target_currency = input("What currency do you want to convert to? ").strip().upper()

        if target_currency in data:
            converted = amount * data[target_currency]
            print(f"\nDollar: {amount} USD")
            print(f"{target_currency}: {converted:.6f}")
        else:
            print("Invalid currency code.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    convert_currency()
