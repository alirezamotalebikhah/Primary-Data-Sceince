import random
import time
namelist = ['alireza' , 'arshia' , 'maryam' , 'sara' , 'nazanin' , 'mohammad' , 'mehrdad' , 'mahsa' , 'tina']
print("Welcom to guess name program")
time.sleep(3)
name = random.choice(namelist).lower()
len_name = len(name)
list_name = list(name)
# print(len_name)
# print(list_name)
def easygame(name , len_name , list_name):
    output=[]
    for i in range(len_name):
        output.append('_')
    print(output)
    max_guess = len_name * 2
    print(f"you have {max_guess} chance to guess")
    num_guess = 0
    num_correct_guess=0
    while num_guess < max_guess :
        print(output)
        guess = input("guess your letter\n").lower()
        for i in range(len_name):
            if name[i] == guess:
                output[i] = guess
                num_correct_guess +=1
        num_guess +=1
        print(f"you have {max_guess - num_guess} chance to guess")
        if num_correct_guess == len_name:
            print("you win , the name is {name}")
            break
        else:
            continue
    if num_guess == max_guess:
        print(f'Sorry , you lose. the correct answer is {name}')        
def hardgame(name , len_name , list_name):
    output=[]
    for i in range(len_name):
        output.append('_')
    print(output)
    max_guess = len_name
    print(f"you have {max_guess} chance to guess")
    num_guess = 0
    num_correct_guess=0
    while num_guess < max_guess :
        print(output)
        guess = input("guess your letter\n").lower()
        correct = False
        for i in range(len_name):
            if name[i] == guess:
                output[i] = guess
                num_correct_guess +=1
                correct = True
        if not correct:
            num_guess +=1
        print(f"you have {max_guess - num_guess} chance to guess")
        if num_correct_guess == len_name:
            print(f"you win , the name is {name}")
            break
        else:
            continue
    if num_guess == max_guess:
        print(f'Sorry , you lose. the correct answer is {name}')        
level = input('which level do you want to play?(hard or easy)\n').lower()
if level == 'easy':
    easygame(name , len_name , list_name)
else:
    hardgame(name , len_name , list_name)




