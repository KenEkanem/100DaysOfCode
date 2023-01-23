print("Welcome to the love calculator!")
name1 =input("What is your name? \n")
name2 =input("What is their name? \n")


name_combined = name1 + name2
lowCaseName = name_combined.lower()

t = lowCaseName.count("t")
r = lowCaseName.count("r")
u = lowCaseName.count("u")
e = lowCaseName.count("e")

true = t + r + u + e

l = lowCaseName.count("l")
o = lowCaseName.count("o")
v = lowCaseName.count("v")
e = lowCaseName.count("e")

love = l + o + v + e

score_str = str(true) + str(love)


love_score = int(score_str)
# print(love_score)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score >=40) and (love_score<=50):
    print(f"Your score is {love_score} you are alright together")
else:
    print(f"your score is {love_score}")