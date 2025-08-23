import random

game = input("which game do you want to play? \n lion & line (input l)\n rock paper scissor(input r)\n :")
def rock():
    hand = input("rock (input r) , paper (input p) , scissor (input s)\n : ")
    handai = random.choice(["rock", "paper", "scissor"])
    if handai == hand:
        print(f" your hand is {hand} and my hand is {handai} it's draw")
    elif (handai == "rock" and hand=="p") or (handai == "paper" and hand=="s") or (handai == "scissor" and hand=="r") :
        print(f" your hand is {hand} and my hand is {handai} nice you win")
    else:
        print(f"your hand is {hand} and my hand is {handai} , sorry you lose like your life")
def line():
    guess = input("guess your coin : lion(input 0) , line(input 1)\n :")
    coin = random.randint(0,1)
    if guess == coin:
        print("high chance , you win")
    else:
        print("low chance , you lose every time")
if game == "l":
    line()
else:
    rock()







