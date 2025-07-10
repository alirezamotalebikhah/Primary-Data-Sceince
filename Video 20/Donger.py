import time
print("welcome to Donger")
time.sleep(5)
print("\n****************")
number=int(input("\n How Many people are in Donger?"))
cost=int(input("\n How Musch Of Cost to pay?"))
sale_parameter = input("\n How Much of discount?(if doesnt Have just press enter)")
if sale_parameter.strip()=="":
    sale_parameter = 0
else:
    sale_parameter = int(sale_parameter)
dong = (cost - cost*(sale_parameter/100))/number
print("\n")
print(f"dong of every person is {dong}")
