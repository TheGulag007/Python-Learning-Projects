#Input function "input()" ask user to enter the data, the data will be stored as string.

food = input("What is your favourite food?: ")
#Since the input is normally stored as string, we can typecast the input function directly if we want to change it to other variable types.
age = int(input("How old are you?: "))

age = age + 1



#You want to use f-string when you want to insert variable together within string.
print(f"Your favourite food is {food}!")
print("HAPPY BIRTHDAY!")
print(f"You're {age} years old")