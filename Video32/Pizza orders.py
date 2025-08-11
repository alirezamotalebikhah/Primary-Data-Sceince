def take_order():

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

    total_price = 0
    orders = []

    while True:
        print("\n--- New Order ---")


        pizza_qty_input = input("How many pizzas? (press Enter for none): ").strip()
        if pizza_qty_input.isdigit() and int(pizza_qty_input) > 0:
            pizza_qty = int(pizza_qty_input)

            pizza_input = input("Which Pizza?\n 1.Peperoni  2.Normal  3.Chicken: ").strip().lower()
            size_input = input("Which size?\n 1.One person  2.Two person  3.Three person: ").strip().lower()
            cheese = input("Extra cheese? yes or no: ").strip().lower()

            pizza_choice = pizza_map.get(pizza_input, pizza_input)
            size_choice = size_map.get(size_input, size_input)

            pizza_price = pizza_prices.get(pizza_choice, 0)
            size_price = size_prices.get(size_choice, 0)
            cheese_price = 3 if cheese in ["yes", "y"] else 0

            subtotal = (pizza_price + size_price + cheese_price) * pizza_qty
            total_price += subtotal
            orders.append(f"{pizza_qty}x {pizza_choice} ({size_choice}) {'+ cheese' if cheese_price else ''} = {subtotal} $")


        drink_qty_input = input("How many drinks? (press Enter for none): ").strip()
        if drink_qty_input.isdigit() and int(drink_qty_input) > 0:
            drink_qty = int(drink_qty_input)

            drink_input = input("Which drink?\n 1.Coca  2.Water  3.Beer: ").strip().lower()
            drink_choice = drink_map.get(drink_input, drink_input)

            drink_price = drink_prices.get(drink_choice, 0)
            subtotal = drink_price * drink_qty
            total_price += subtotal
            orders.append(f"{drink_qty}x {drink_choice} = {subtotal} $")


        more = input("Do you want to add another order? (yes/no): ").strip().lower()
        if more not in ["yes", "y"]:
            break


    print("\n--- Final Order Summary ---")
    for o in orders:
        print(o)
    print(f"Total Price: {total_price:,.0f} $")


print("Welcome to our Pizza Shop")
take_order()
