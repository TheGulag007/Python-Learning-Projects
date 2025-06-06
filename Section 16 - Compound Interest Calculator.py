#create a program to tell you what the new balance will be after acrewing interest over years
#formula -> A = P(1 + r/n)^t
#A = final amount, P = initial balance, r = interest rate, t = period of time elapsed

principle = 0
interate = 0
year = 0

#We can also write a variation of this by using "while True:", then add the "else: break" to exit from this loop or else it will become infinite loop
while True:
    principle = float(input("Please enter your initial balance: "))
    if principle <= 0:
        print("Your initial balance can't be 0 or lower")
    else:
        break

while interate <= 0:
    interate = float(input("Please enter the bank interest rate: "))
    if interate <= 0:
        print("The interest rate can't be 0 or lower")

while year <= 0:
    year = int(input("Enter the time in years: "))
    if year <= 0:
        print("Time can't be 0 or lower")

total = principle * pow((1 + interate / 100), year)

print(f"Your balance after saving for {year} years will be: ${total:.2f}")