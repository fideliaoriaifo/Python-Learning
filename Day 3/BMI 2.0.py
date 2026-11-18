# write a program that interpretes the BMI based on a users weight and height. The BMI is calculated 
# by dividing a persons weight (in kg) by the square of their height (in m).

weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")