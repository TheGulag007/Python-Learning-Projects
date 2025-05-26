#Making a Python Calculator using if statements

#user select an operator (+ - * /)
operator = input("Please enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

#You can print the result of arithmetics
if operator == "+":
    print(round(num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print(f"Your operator {operator} is not valid. Calculator only works on +, -, *, / operators!")
