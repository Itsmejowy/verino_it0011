file_path = "C:\Users\JUDITH\OneDrive\Documents\verino_it0011\verino_it0011\TME"

with open(file_path, "r") as file:
    lines = file.readlines()
    line_number = 1
    for line in lines:
        numbers = line.strip().split(',')
        total = 0
        for num in numbers:
            total = total + int(num)
        sum_str = str(total)

        if sum_str == sum_str[::-1]:
            result = "Palindrome"
        else:
            result = "Not a palindrome"
        print ("----------------------------------------------------------")
        print(f"Line {line_number}: {line.strip()} (sum {total}) - {result}")
        print ("----------------------------------------------------------")
        line_number = line_number + 1