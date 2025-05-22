#Typecasting is how we convert ones variable type to another. Ex: String -> Int, Int -> Float
#We typecast variable by using: str(), int(), float(), bool()

name = "GottGulack"
age = 18
gpa = 7.0
is_student = True
Faker = ""
food = "Boiled egg1"

gpa = int(gpa)

print(type(gpa))
print(gpa)
#When typecast float into int, the decimal number will get cut down (even if it's a 0.9)

age = float(age)

print(type(age))
print(age)
#Typecasting int into float will add decimal point to the number Ex: 25 -> 25.0

age = str(age)

age += "1"
print(type(age))
print(age)
#When we typecast variable into something, the variable will act as that type instead of previous one immediately. (The 18.0 becomes 18.01 after adding "1" instead of 19.0)

name = bool(name)

print(type(name))
print(name)
#Typecasting string into boolean will always give "True", it will only give "False" if the string value is empty (This could be used for when we want to set remind system that the user isn't entering their name yet)

Faker = bool(Faker)

print(type(Faker))
print(Faker)

food = int(food)

print(type(food))
print(food)
#You can only typecast string into int if the value only contains integers