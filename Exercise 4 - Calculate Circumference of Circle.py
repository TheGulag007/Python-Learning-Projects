#Make code that calculate the Circumference of Circle
import math
#Circum Circle = 2 * math.pi * r

print("CIRCLE CIRCUMFERENCE CALCULATOR")
print("--------------------------------")
r = float(input("Enter your circle radius (cm): "))

#don't forget that input data will always be string
circum_circle = 2 * math.pi * r
print(f"The circumference is: {round(circum_circle, 3)} cm²")

#round(x, 3) means rounding x to nearest thousandth
#the number behind x "(x, 3)" means the place of decimal we want to round nearest to