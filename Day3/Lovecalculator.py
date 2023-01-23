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

love_score = str(true) + str(love)
print(love_score)