
# ADDING TWO DIGIT INPUTS TOGETHER

two_digit_number = input("Type a two Digit number \n")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
number = int(first_digit) + int(second_digit)
print(number)



# MATHEMATICAL OPERATIONS

# PEMDAS
# ()
# **
# */
# +-
# print(3*3+3/3-3)

# A SIMPLE BMI CALCULATOR

height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")
bmi = int(weight) / float(height) ** 2
bmi_as_integer = int(bmi)

print("Your bmi is: " + str(bmi_as_integer))

# NUMBER MANIPULATION AND F STRING IN PYTHON


# CALCULATING TIME LEFT IN WEEKS AND MONTHS
age = input("What is yout age?: ")
age_int = int(age)
age_left = 90 - age_int
days_left = age_left * 365
weeks_left = age_left * 52

months_left = age_left * 12
# print(months_left)

print(f"You have {days_left} days {weeks_left} weeks, and {months_left} months left")


print("Welcome to the tip calculator")

bill = input("What is the total bill?")
percentage_tip  = input("What percentage tip would you like to give? 10, 12, or 15?: ")

bill_float = float(bill)
percentage_float = float(percentage_tip)

percentage_cal = bill_float / 100 * percentage_float

num_of_people = int(input("how many people to split the bill?: "))

percentage_split = percentage_float / num_of_people

bill_split = bill_float / num_of_people

new_bill = bill_split + percentage_split
roundedbill = round(new_bill,2)
print(f"Each person should pay ${roundedbill}")








