name1 = input("what is your name? ").lower()
name2 = input("what is your partner name? ").lower()
combinedname = name1 + name2
def count_words(word: str):
    total = 0
    for ch in word:
        total += combinedname.count(ch)
    return total
love = count_words("love")
true = count_words("true")
lovescore = int(str(love) + str(true))
print(lovescore)
if lovescore <= 5:
    print("mismatch")
elif 6 <= lovescore <= 50:
    print("no hope , maybe it's okay")
elif 51 <= lovescore <= 90:
    print("nice , find your match")
else:
    print("it's legendry Love")


