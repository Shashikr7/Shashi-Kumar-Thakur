class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        else:
            return "Invalid operation"



a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operation (add/subtract/multiply/divide): ")

calc = Calculator()
print("Result:", calc.calculate(a, b, op))
