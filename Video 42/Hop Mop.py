import time

def print_rules(data, en_number):
    divisors = sorted(data.keys(), reverse=True)
    for num in range(1, en_number + 1):
        output = ""
        for divisor in divisors:
            if num % divisor == 0:
                output = data[divisor]
                break
        if output == "":
            print(num)
        else:
            print(output)
        time.sleep(0.5)

n = int(input("How many rules do you want to define?\n"))
data = {}
for _ in range(n):
    idx = int(input("What's the divisor?\n"))
    val = input("What's it called?\n")
    data[idx] = val

print(f"\nYour rules are: {data}")
en_number = int(input("Enter your last number:\n"))

print("\nResult:")
print_rules(data, en_number)
