#Conditional expression is a one line shortcut for if-else statements
#We can print or assign one of two values based on a condition
#For Ex: X if conditions else Y

num = -5
print("Positive" if num > 0 else "negative")

num = 3
print("Even" if num % 2 == 0 else "Odd")

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

age = 14
status = "Adult" if age >= 18 else "Minor"
print(status)

temperature = 27
temp_feel = "Hot" if temperature > 27 else "Cold"
print(temp_feel)

user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)