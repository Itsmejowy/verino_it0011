file_path = r"C:\Users\JUDITH\Downloads\numbers.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    line_number = 1
    for line in lines:
        numbers = [num.strip() for num in line.strip().split(',') if num.strip()]
        total = sum(int(num) for num in numbers)  # Convert to integers and sum
        sum_str = str(total)

        result = "Palindrome" if sum_str == sum_str[::-1] else "Not a palindrome"

        print(f"Line {line_number}: {line.strip()} (sum {total}) - {result}")
        line_number += 1
