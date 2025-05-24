#This section cover some basic arithmetics, functions, and few exercises

friends = 0
robux = 0
LP = 5
apple = 10
xerath = 2
eggs = 40

#The friends +=1 is short type of friends = friends + 1
friends += 1

#The robux -= 2 is short type of robux = robux -2
robux -= 2

#"X *= n" -> X = X * n
LP *= 3

#"X /= n" -> X = X / n BUT the result are in float instead of int
apple /= 10

#"X **= n" -> X = X ** n
xerath **= 3

#Modulus "%" is the calculation method used to find the remainder of the division
eggs %= 3
#Modulus is commonly used to find whether the number is even or odd (It's odd if it have remainder)

print(f"You have {friends} friends")
print(f"You have {robux} robux")
print(f"You lost {LP} LP today")
print(f"You eat {apple} apple per day")
print(f"You've played {xerath} hours of Xerath this week")
print(f"There will always be {eggs} eggs left in your fridge")

#Next we will cover some built-in math functions

x = 33.14
y = -4
z = 5

#Use round() to round number to the nearest one
#Use abs() to find the absolute value of the variable
result1 = round(x) + abs(y)
print(result1)

#Use pow() to base 1st variable exponented with 2nd variable Ex: pow(4, 5) = 4^5
result2 = pow(abs(y), z)
print(result2)

#Use max() to find the maximum value in the listed variables
result3 = max(x, y, z)
print(result3)

#Use min() to find the minimum value in the listed variables
result4 = min(x, y, z)
print(result4)

#You can import math module into python to get the more standard value of constants that mostly used in math
import math
x = 9
y = 4.1
z = 5.9999999
print(math.pi)
print(math.e)

#math.sqrt is the square root function
result5 = math.sqrt(x)
print(result5)

#math.ceil is the function to always round the number up
result6 = math.ceil(y)
print(result6)

#math.floor is the function to always round the number down
result7 = math.floor(z)
print(result7)
