#While loop executes code WHILE some condition remains true

#While loop can execute the code forever, until the condition is no longer met
#If we didn't give ourselve an exit strategy (condition to get out of while loop), else you will be stuck in the infinite loop
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = input("Enter your age: ")

print(f"You are {age} years old")

food = input("Enter your favourite food (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
#For now, while loop can be use similar to if statement, but loop forever until the user follow the prompt given.