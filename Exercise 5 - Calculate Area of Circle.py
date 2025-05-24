#Make a calculator for area of circle
#Circle A = math.pi * r²
import math

print("CIRCLE AREA CALCULATOR")
print("----------------------")
r = float(input("Enter your circle radius (cm): "))
#you can also use pow(radius, 2) in this section
#recall: pow(radius, 2) = radius^2
r **= 2

result = math.pi * r
print(f"The Area of Circle is {round(result, 3)} cm²")