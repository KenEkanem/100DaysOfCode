# A simple BMI Calculator 2.0

height = float(input("Enter your height in m:\n"))
weight = float(input("Enter your weight in kg:\n"))
bmi = round(weight / height ** 2)
# bmi = 28
  
if bmi < 18.5:
    print(f"Your BMI is {bmi_as_integer}, you are Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
