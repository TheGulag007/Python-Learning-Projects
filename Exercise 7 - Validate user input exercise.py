#We want user to enter a valid username with these following rules:
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")
if len(username) > 12 and username.find(" ") >= 0:
    print("Your username can't be more than 12 characters and must not have space bars")
elif len(username) > 12 or not username.find(" ") == -1 or username.isalpha() == False:
    print(f"Please check if your username: {username} are not met in which of these rules:")
    print("1. username is no more than 12 characters")
    print("2. username must not contain spaces")
    print("3. username must not contain digits")
else:
    print(f"Welcome {username}")

ex = "GottGulack"
ex = ex.count("P")
print(ex)