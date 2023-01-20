# CONDITIONAL STATEMENTS - CONTROL FLO WITH IF ELSE AND CONDITIONAL OPERATORS

# Examples 

print("Welcome to the rollercoaster!")
height = int(input("Please input your height in cm "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5 dollars")
    elif age <= 18:
        print("Please pay $7")    
    else:
        print("Please pay $12")
else:
    print("Sorry! You have to grow taller befor you can ride")



# number = int(input("Which number do you want to check?"))

# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# NESTED STATEMENTS IF STATEMENTS (ELIF STATEMENTS)

