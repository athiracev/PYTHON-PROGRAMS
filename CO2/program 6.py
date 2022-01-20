#Count the number of charecters in a string


str = input("Enter a string: ")
count = 0
for i in str:
    if i.isalpha():
        count += 1

print("Number of characters in "+str+" is: ", count)