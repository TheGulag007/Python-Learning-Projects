#Madlibs game is a word game where you create a story by filling the blank with random words

print("WELCOME TO MADLIBS GAME")
print("---------------------")
print("Today I went to a -adj1- zoo.")
print("In an exhibit, I saw a -noun1-.")
print("-noun1- was -adj2- and -verb1-")
print("I was -adj3-!")
print("---------------------")
print("Note: Adjective is used for describing something")

adj1 = input("Enter an adjective1 (description): ")
noun1 = input("Enter a noun1 (person, place, or thing): ")
adj2 = input("Enter an adjective2 (description): ")
verb1 = input("Enter a verb1 (-ing verb): ")
adj3 = input("Enter an adjective3 (description): ")

print(f"Today I went to a {adj1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adj2} and {verb1}")
print(f"I was {adj3}!")
