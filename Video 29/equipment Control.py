import time
print("Welcome to equipment Control program\n")
time.sleep(3)
deg=int(input("Please enter the number of degrees:\n "))
AQI = int(input("Please enter the AQI:\n "))
window='0'
cooler='0'
heater='0'
air_conditioner='0'
if deg >30:
    heater='0'
    if AQI>100:
        cooler='1'
        air_conditioner='1'
    elif AQI<50:
        window='1'
    elif 50<=AQI<=100:
        cooler='1'
else:
    heater='1'
    cooler='0'
print(f"window is {window}\n"
      f"cooler is {cooler}\n"
      f"heater is {heater}\n"
      f"air_conditioner is {air_conditioner}\n")

