import random

which = input("Where is the goal? In right or left hand? (R and L): ")

def lowchance():
    prizes = {
        1: 'iPhone',
        2: 'BMW', 
        3: 'Rich Partner'
    }
    i = random.randint(1, 10)
    
    if i in prizes:
        print(f"Your prize is {prizes[i]}")
    else:
        print("Sorry, see you next time")

def highchance():
    prizes = ['iPhone', 'BMW', 'Electrical Guitar', 'Loyal Friend']
    i = random.randint(0, 3)
    print(f"Your prize is {prizes[i]}")

if which.upper() == "R":
    lowchance()
else:
    highchance()