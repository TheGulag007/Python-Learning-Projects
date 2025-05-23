#Exercise 1 - Making a rectangle area calculator
#Rectangle A = W * L
print("THE RECTANGLE AREA CALCULATOR")
length = float(input("Rectangle Length: "))
width = float(input("Rectangle Width: "))

area = length * width

#The superscript of ^2 typing command in window is Alt+Num(0178)
print(f"The rectangle area is {area} cm²")
print(type(area))
#Note: Since the calculator involve in geometry, float is a better option than int
