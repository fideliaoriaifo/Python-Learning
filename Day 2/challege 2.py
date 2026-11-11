#write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi_dec = weight / (height ** 2)
#bmi to be a whole number, we can use the round() function to round the bmi to the nearest whole number.
bmi = round(bmi_dec)
print(bmi)

#how to use the exponent function in python.