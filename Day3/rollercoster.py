print("Welcome to the rollercoaster!")
height = int(input("Please input your height in cm "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5 dollars")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us")    
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry! You have to grow taller befor you can ride")