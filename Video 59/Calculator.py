class Calculator:
    def __init__(self):
        self.history = []
        self.result = None

    def operate(self, operator, number):
        if self.result is None:  # first number
            self.result = number
            return self.result

        if operator == "+":
            self.result += number
        elif operator == "-":
            self.result -= number
        elif operator == "*":
            self.result *= number
        elif operator == "/":
            if number == 0:
                self.history.append(f"{self.result} / {number} = Error (division by zero)")
                return "Error"
            self.result /= number
        else:
            return "Invalid operator"

        self.history.append(f"{self.result}")
        return self.result

    def show_history(self):
        print("\n--- Operations History ---")
        for i, step in enumerate(self.history, start=1):
            print(f"Step {i}: {step}")
        print(f"\nFinal Result = {self.result}")


def main():
    calc = Calculator()

    # first number
    num = float(input("Enter first number: "))
    calc.result = num
    calc.history.append(str(num))

    while True:
        operator = input("Enter operator (+, -, *,, /) or '=' to show result: ")
        if operator == "=":
            calc.show_history()
            break
        num = float(input("Enter next number: "))
        calc.operate(operator, num)


if __name__ == "__main__":
    main()
