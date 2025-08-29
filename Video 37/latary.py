import random
names=[]
print("Enter your list name:\n")
print("-"*40)

while True:
    name = input("Enter name: ").strip()
    if name.lower() == "exit":
        break
    if name :
        names.append(name)
        print(f"{name} added")
    else:
        print("invalid name")
print(names)
size = len(names)
winner = random.randint(0,size-1)
print(f"winner is {names[winner]}")


