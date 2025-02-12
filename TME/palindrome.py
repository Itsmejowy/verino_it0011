def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

process_file("numbers.txt")
