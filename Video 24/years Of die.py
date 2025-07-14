from datetime import datetime, timedelta

today = datetime.today()

print("How long do you think you'll live from today?")
print("1. Enter remaining days")
print("2. Enter remaining weeks")
print("3. Enter remaining months")
choice = input("Choose an option (1/2/3): ")

amount = int(input("Enter the amount: "))

if choice == "1":
    death_date = today + timedelta(days=amount)
elif choice == "2":
    death_date = today + timedelta(weeks=amount)
elif choice == "3":
    death_date = today + timedelta(days=amount * 30)
else:
    print("Invalid choice.")
    exit()

remaining_days = (death_date - today).days
remaining_weeks = remaining_days // 7
remaining_months = remaining_days // 30
remaining_years = remaining_days // 365

print(f"\n🕯 Estimated death date: {death_date.date()}")
print("⏳ Estimated time left from today:")
print(f"{remaining_years} years")
print(f"{remaining_months} months")
print(f"{remaining_weeks} weeks")
print(f"{remaining_days} days")
