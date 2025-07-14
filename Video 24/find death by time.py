import time
from datetime import datetime, timedelta
from time import sleep
current_age = int(input("Enter current age: "))
death_age = int(input("Enter death age: "))
if current_age > death_age:
    print("Rest in peace")
else :
    remain_years = death_age - current_age
    remain_days = remain_years*365
    remain_weeks = remain_days//7
    remain_mouth = remain_years*12
print("times to die Alone!")
time.sleep(3)
print(f"{remain_mouth} mounths")
print(f"{remain_weeks} weeks")
print(f"{remain_days} days")