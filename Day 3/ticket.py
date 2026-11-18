# write a program that asks for the height of a person and allows them to ride only if their height 
# is greater than 120cm

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster!")
    # ask for age and ask for $12 if they are 18 or older, $7 if they are under 18 years old. 
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You are not tall enough to ride the roller coaster.")