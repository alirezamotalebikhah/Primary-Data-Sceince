number = input("Enter the number:\n")
digits=[]
for digit in number:
    digits.append(int(digit))
print(digits)
sum_digits = sum(digits)
print("Sum of digits:", sum_digits)

