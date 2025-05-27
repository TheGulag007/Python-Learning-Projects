#Create a weight converter
#1 kg = 2.20462 lbs

print("KG TO LB CONVERTER")
print("----------------------")
weight = float(input("What is your weight?: "))
unit = input("Is this weight in kg or lb? (kg/lb): ")
k2p = 2.20462
p2k = 0.453592

if unit == "kg":
    result = round(weight * k2p, 2)
    print(f"You weight is {result} lbs")
elif unit == "lb":
    result = round(weight * p2k, 2)
    print(f"You weight is {result} kg")
else:
    print("Please insert the correct unit (kg/lb)")