#You can access the element of sequence by using indexing operator "[]"
#Ex: [start: end: step]

credit_number = "1234-5678-9012-3456"

#Recall: Computer starts with 0, that's why indexes always start with 0
#if you just type in one thing without any colon, it'll assume you want to mention only "start" in the [start: end: step]
print(credit_number[1])

#by pointing out where to end, the code will run to the list until reaching the end point, it will not list the end point in result 
#Ex: When using [0:4], instead of 1234- it will only show 1234
print(credit_number[0:4])
#you can also just type ":4" in this case, python will just assume you want the starting point of the index as "start"

print(credit_number[5:9])

#when you type something like [5:], python will assume you need listing from 5 to the very end of the string
print(credit_number[5:])

#using negative index like "[-1], [-2], [-3],..."" will list your string starting from the very end and so on.
print(credit_number[-1])
print(len(credit_number))

#negative indexes can also works with python assumes too, until before the very last string character
print(credit_number[:-1])

#the "step" in the string indexing method [start: end: step] works as how you want to count the string character
#Ex: the [::2] will count every 2nd character
print(credit_number[::2])

#practice: Make a code that count only the last 4 digits of the credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#practice2: Reverse the credit card numbers to 6543-2109-8765-4321
reverse_card = credit_number[::-1]
print(reverse_card)