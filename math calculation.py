class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def get_input(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    def add(self):
        self.result = self.num1 + self.num2
        print("Result: ", self.result)

    def subtract(self):
        self.result = self.num1 - self.num2
        print("Result: ", self.result)

    def multiply(self):
        self.result = self.num1 * self.num2
        print("Result: ", self.result)

    def divide(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
            print("Result: ", self.result)
        else:
            print("Error: Division by zero is not allowed.")

def main():
    calc = Calculator()
    calc.get_input()
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Choose an operation (1/2/3/4): ")
    if choice == '1':
        calc.add()
    elif choice == '2':
        calc.subtract()
    elif choice == '3':
        calc.multiply()
    elif choice == '4':
        calc.divide()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()