# logical operators evalutates mutliple conditions (or, and, not)

#logical operator (or) will run the code if one of the condition were true
eggs = 23
is_cooked = True

if eggs > 34 or eggs < 0 or is_cooked == True:
    print("Let's order some eggs today")
else:
    print("The eggs are still available in the fridge")

#logical operator (and) will run the code if all the conditions were true
Bachira_goat = False
Bachira_best = True

if Bachira_goat == True and Bachira_best == True:
    print("Bachira >>>>>>>>>>>>>>>>> Shidou, Rin, Isagi, Universe")
else:
    print("The show sucks and I won't watch it again")
#You can add as many conditions as you like for any logical operators

#logical operator (not) will run the code if the condition is NOT false, or NOT true

Shen_op = True
Aatrox_op = True

if Shen_op == True and not Aatrox_op == True:
    print("The world is doomed, Lynerun will omega abuse this to oblivion")
elif Aatrox_op == True and not Shen_op == True:
    print("Lynerun will definitely perma ban Aatrox for the whole patch")
else:
    print("Decent patch")