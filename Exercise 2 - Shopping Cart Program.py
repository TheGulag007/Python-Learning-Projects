#Exercise 2 - Making a shopping cart program

item = input("What item would you like to buy?: ")
#We use float because there might be some cents in the price tag of items
price = float(input("What is the price?: $"))
quantity = int(input("How many of them would you buy?: "))

total = price * quantity

print(f"The total price of {quantity} {item} is ${total}")