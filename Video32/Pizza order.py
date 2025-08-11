print("Welcome to our Pizza Shop")
type_input = input("Which Pizza would you like to order?\n 1.peperoni 2.Normal 3.chicken\n ").strip().lower()
size_input = input("Which size would you prefer to order?\n 1.one person 2.two person 3.three person ").strip().lower()
cheese = input("Do you like extra cheese? yes or no ").strip().lower()
drink_input = input("Which drink would you like to order?\n 1.Coca 2.Water 3.Beer ").strip().lower()

pizza_prices = {
    "peperoni": 10,
    "normal": 7,
    "chicken": 12,
}
size_prices = {
    "one person": 2,
    "two person": 3,
    "three person": 5,
}
drink_prices = {
    "coca": 5,
    "water": 3,
    "beer": 6,
}
pizza_map = {
    "1": "peperoni",
    "2": "normal",
    "3": "chicken",
}
size_map = {
    "1": "one person",
    "2": "two person",
    "3": "three person",
}
drink_map = {
    "1": "coca",
    "2": "water",
    "3": "beer",
}


pizza_choice = pizza_map.get(type_input, type_input)
pizza_price = pizza_prices.get(pizza_choice, 0)

size_choice = size_map.get(size_input, size_input)
size_price = size_prices.get(size_choice, 0)

cheese_price = 3 if cheese in ["yes", "y"] else 0

drink_choice = drink_map.get(drink_input, drink_input)
drink_price = drink_prices.get(drink_choice, 0)

total_price = pizza_price + size_price + cheese_price + drink_price

print("\n--- Order Summary ---")
print(f"Total Price: {total_price:,.0f} $")

