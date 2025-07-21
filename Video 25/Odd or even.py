print("Welcome to Odd or Even Program")
num=input("\n Enter your number: ")
last_digit=int(num[-1])
print(f"\nbecause your last number is {last_digit}")
if last_digit % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")