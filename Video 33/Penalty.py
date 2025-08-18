import random
light = random.choice(['red', 'green'])
penalty_light= 50
penalty_drunk= 500
penalty_tech = 150
cross= input("Do ypu Cross the street? 'Y' or 'N'\n")
drunk = random.choice(['sober','high as f*ck'])
id_cart = int(input("how many years old ?"))
penalty=0
if cross=='Y' and light=='red':
    penalty += penalty_light
    if not drunk=='sober':
        penalty += penalty_drunk
        if id_cart < 18 :
            penalty += penalty_tech
    print(f"you have {penalty} penalties\n"
          f"you cross the street when light is {light}\n"
          f"you are {drunk}\n"
          f"you have {id_cart} years old")
else:
    print(f"you can be {drunk} and have {id_cart} years old and have {penalty} penalties\n"
          f"when light is {light}\n or {cross} cross the street when light is {light}\n")
