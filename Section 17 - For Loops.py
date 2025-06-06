#for loop will execute code for a FIXED number of times, unlike while loop which goes on forever.
#you can iterate anything that is consider iterable: range, string, sequence, etc.

#for loop is better than while loop in situation where you need to loop for a fixed number of times

#while loop is better if you want to execute something possibly an infinite amount of times

#the second number is exclusive, so if we want it to count from 1-10, we need to type 11
#there is also a reversed() function that make we count in reverse
for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR!")

#the range is similar to the string indexing, not only you can locate the start and ending point, you can also specify the step it listing
for y in range(1, 11, 2):
    print(y)

#you can also iterate with strings
credit_num = "1234-5678-9012-3456"

for x in credit_num:
    print(x)

#there are 2 important keywords for both for loop and while loop: continue and break

#"continue" will skip over the specify value of x

#"break" will stop the loop entirely once it reaching the specify value of x
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
