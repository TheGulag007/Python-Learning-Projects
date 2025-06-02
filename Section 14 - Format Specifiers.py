#format specifiers = {value:flags}, this will format a value based on what "flags" are inserted

#.(number)f = round to that many decimal places
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print("The .(number)f format, it will round to that many decimal places")
print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")
print("--------------------------------------")

#:(number) = allocate that many spaces
#you can also pad the allocated spaces with 0s by typing :(0number)
print("The :(number) format, this will allocate that many spaces")
print(f"Price 1 is {price1:010}")
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:010}")
print("--------------------------------------")

#:< = left justify
("The :< format, this will left align the value like how docs left align works")
print(f"Price 1 is {price1:<10}")
print(f"Price 2 is {price2:<10}")
print(f"Price 3 is {price3:<10}")
print("--------------------------------------")
#:> = right justify
("The :> format, similar to left align, but on the right instead of left")
print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:>10}")
print("--------------------------------------")

#:^ = center align
("The :^ format, it's the center align like how it's work in docs")
print(f"Price 1 is {price1:^10}")
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")
print("--------------------------------------")

#:+ = use a plus sign to indicate postive value
("The :+ format, use it to display (+) sign on positive values, it doesn't effect on negative values.")
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")
print("--------------------------------------")

#:= = place sign to leftmost position
("The := format, use it to place any sign to leftmost position, doesn't effect values that already have one Ex: negative values (-97, -89324)")
print(f"Price 1 is {price1:=+}")
print(f"Price 2 is {price2:=+}")
print(f"Price 3 is {price3:=+}")
print("--------------------------------------")

#: = insert a space before positive number
("The :spacebar  format, use it to insert space before positive numbers")
print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")
print("--------------------------------------")

#:, = comma separator
("The :,  format, use it to insert comma to separated each thousand places")
price1 = 2235236306
price2 = 431232
price3 = 21413432

print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")
print("--------------------------------------")

#we can also use multiple format at the same time (max of 3)

print(f"The Price 1 is ${price1:+,.2f}")
