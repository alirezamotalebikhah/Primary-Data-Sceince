deg = int(input("Enter degree:\n "))
rate = int(input("Enter rate of pullotion:\n "))
if deg < 30:
    print("Cooler get off\nheater is on")
else:
    if rate  > 100:
        print("cooler is on")
    else:
        print("open the window")
