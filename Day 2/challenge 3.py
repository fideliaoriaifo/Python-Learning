#write a program that tells us how many weeks we have left, if we live until 90 years old. It will take your current age as the input and output a message with our time left in this format:
#You have x weeks.
current_age = int(input("What is your current age? "))
years_left = 90 - current_age
weeks_left = years_left * 52

print(f"You have {weeks_left} weeks.")