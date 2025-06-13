import random as rd

guess_num = rd.randint(0, 100)
count = 0
low = 0
high = 100
my_num = -1  

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")

while my_num != guess_num:
    if count == 0:
        my_num = int(input("Enter your guess: "))
    else:
        if my_num < guess_num:
            low = my_num + 1
        elif my_num > guess_num:
            high = my_num - 1
        my_num = int(input(f"Try again! Guess between {low} and {high}: "))

    count += 1

print(f"✅ Congratulations! You guessed the number {guess_num} in {count} tries! 🎉")
