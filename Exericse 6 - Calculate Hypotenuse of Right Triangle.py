#Make a calculator to calculate hypotenuse of right triangle
import math
#Hypotenuse RTri = math.sqrt(a²+b²)

print("RIGHT TRIANGLE HYPOTENUSE CALCULATOR")
print("------------------------------------")

a = float(input("Enter the Adjacent side (cm): "))
b = float(input("Enter the Opposite side (cm): "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse is {round(hypotenuse, 3)} cm")