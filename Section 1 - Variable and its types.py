print("I love League of Legends!")
print("The game is so bad it's insane!")
#This is a comment in Python programming

#Variable = container for a value, which also behave like the value its contain.
#There are 4 types of variable = String, Int, Float, and Boolean

#Anything inside the "" is considered as String Ex: "Banana", "123", "🔥🤔"
First_name = "GottGulack"
Food = "Boiled Beans"
Email = "thisgmailisnotreal@gmail.com"

#Use f-strings to express some text with variable
print(f"Hello {First_name}")
print(f"You like {Food}")
print(f"Your email is {Email}")

#Int is integers Ex: 24153, 423, -325
age = 12
quantity = 125
latest_lp = -23

print(f"Your body age is {age} years old")
print(f"You have {quantity} Robux in your account")
print(f"Your last LoserQueue result was {latest_lp} LP")

#Float is similar to int, but with decimals
MC_version = 1.21
skin_price = 249.99
running_distance = 6.03

print(f"You think that Minecraft version {MC_version} is the best one so far")
print(f"The latest Mordekaiser skin was only ${skin_price}!")
print(f"You ran {running_distance} km yesterday!")

#Boolean is true or false
# The Boolean is more likely to use internally within the coding program (Such as for if statements) rather than output directly like the 1st example
brain_dmg = True

print(f"Does Lynerun has brain damage?: {brain_dmg}")

#The if statement will run the code in "if" section if Boolean were True, it will run the code in "else" section if Boolean were False
if brain_dmg:
    print("Shen is OP and Lynerun is abusing him")
else:
    print("Please buff Aatrox, Smolder, and Kayle RIOT!")

Briar_dtier = False
if Briar_dtier:
    print("Still, Nerf Briar!")
else:
    print("Nerf Briar!")

dis_online = True
if dis_online:
    print("Discord meeting incoming")
else:
    print("Enoguh League for today")