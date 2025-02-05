# user input
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

#calculation
bmi=weight/(height**2)

if bmi < 18.5:
    classification="Underweight"
elif  bmi < 25:
    classification="normal weight"
elif bmi < 30:
    classification="Overweight"
elif bmi < 40:
    classification="Obesity"

print(f"Your BMI is{bmi},which is  considerd {classification}")