height = float(input("Enter your height in cm:\n"))
weight = float(input("Enter your weight in kg:\n"))
height_m = height / 100
BMI = weight / (height_m ** 2)
print(f"With the height {height} cm and weight {weight} kg, your BMI is {BMI:.2f}\n")
if BMI < 18.5:
    print("Kambud vazn")
elif 18.5 <= BMI < 25:
    print("Ideal")
elif 25 <= BMI < 30:
    print("Normal")
else:
    print("Ezafe vazn ya obes")
