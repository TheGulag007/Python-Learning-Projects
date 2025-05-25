#if statement will do some code only IF the condition for that is true. ELSE it will do else code.

age = int(input("Input your age: "))

#any code under the if statement SHOULD be indented
if age >= 18:
    print("You are now signed up!")
#we can also add more condition before reaching else statement. You can add as many elif statments as you want
elif age < 0:
    print("You haven't been born yet!")
#the order of if statements is important, for example this will still show the "You are now signed up" because the age 101 still met the condition of 1st if statement.
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You must be 18+ years old to sign up")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name!")
else:
    print(f"Hello {name}")

#You can use boolean as a condition for if statement

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

shenbalance = False

if shenbalance:
    print("This champion is fair and balanced")
else:
    print("53% win rate | 15% pick rate | 17% ban rate in MASTER+ EUW")