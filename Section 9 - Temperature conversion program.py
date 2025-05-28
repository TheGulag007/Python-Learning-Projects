print("CELCIUS TO FARENHEIT CALCULATOR")
print("-------------------------------")
unit_temp = input("What is your unit of temperature (C/F)?:")
temp = float(input("Enter the temperature: "))

#(C * 9 / 5) + 32 = F
#(F - 32) * 5 / 9 = C
if unit_temp == "C":
    result = round((temp * 9 / 5) + 32, 2)
    print(f"The temperature is {result} °F")
elif unit_temp == "F":
    result = round((temp - 32) * 5 / 9, 2)
    print(f"The temperature is {result} °C")
elif unit_temp == "c":
    print("Make sure your unit is in capital letter (C)")
elif unit_temp == "f":
    print("Make sure your unit is in capital letter (F)")
else:
    print(f"Your {unit_temp} unit is not valid, please select the mentioned unit (C/F)")

#You can also write "pass" for code under the if statements if you don't know what to write yet but you want to create some structure of the code first

baban ="ggez"

if baban == "ggez":
    pass
else:
    pass