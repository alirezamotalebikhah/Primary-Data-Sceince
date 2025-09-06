
def sumnumber(st_number, en_number , number):
    sum= 0
    number_u = st_number if st_number % number == 0 else st_number + (number - st_number % number)
    for i in range(number_u , en_number , number):
        sum += i
    return sum , number_u 
print("Hello to sum program\n")
st_number = int(input("enter your start number ; \n"))
en_number = int(input("enter your last number :\n"))
number = int(input("number of divisble : \n"))
sum , number_u = sumnumber(st_number , en_number , number)
print(f"sum of number start from {number_u} and end with {en_number} with divide in {number} equal:\n{sum}")