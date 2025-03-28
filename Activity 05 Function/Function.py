def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'X':
            print("Exiting the program. Goodbye!")
            break

        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))

                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiate(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)

                if result is not None:
                    print(f"Result: {result}")

            except ValueError:
                print("Error: Please enter valid integer values.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()