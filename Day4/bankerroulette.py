import random

test_seed = int(input("Please input a seed number: "))
random.seed(test_seed)


namesAsCSV = input("Give everybody's names, seperated by a comma: ")
names = namesAsCSV.split(",")

# num_items = len(names)
# random_choice = random.randint(0, num_items -1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the nmeal today")



