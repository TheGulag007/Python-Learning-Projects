#len() function will count how many letter are there in that string (it also count spacebar as letter)
name = input("Enter your full name: ")
result = len(name)
print(result)

#.find() will find the first occurence of a given character
#when working with index, the first character begins at 0 instead of 1
#Ex: the .find will show result of " " in the Aa trox as 2 instead of 3 (because A = 0, a = 1 " " = 2,...)
#The capitalised letter are different from the non-capitalised one (A =/= a)
result_find = name.find("g")
print(result_find)

#.rfind() will find the last occurence of a given character
#Ex: .rfind("t") of Gottgulack will show 3 instead of 2
#both .find and .rfind will return -1 if there are no result
result_find = name.rfind("t")
print(result_find)

#we can capitalised the first letter in the string by using the .capitalise()
cappa = name.capitalize()
print(cappa)

#.upper() will make all letter in the string an uppercase
chungus = "omega124"
print(chungus.upper())

#.lower() will make all letter in the string a lowercase
big = "ALLCAPFR"
print(big.lower())

#.isdigit() will return true if the string ONLY contains digits, else it will return false
#the spacebar is not counted as digits
digi = "123 543"
print(digi.isdigit())

#.isalpha() works like .isdigit() but only return true if string ONLY contains alphabets
#the spacebar is not counted as alphabet character (This can make .isalpha return false even though there are pure alphabets)
alpha = "banana"
print(alpha.isalpha())

#.count() will count the given character of that string
phone_number = input("Enter your phone number: ")
result = phone_number.count("-")
print(result)

#.replace() will replace the given character to that string
#.replace() is one of the most useful string methods
phone_number = phone_number.replace("-", " ")
print(phone_number)

#if you want a comprehensive list of string method available, use print(help(str))
print(help(str))