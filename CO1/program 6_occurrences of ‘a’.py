# Store a list of first names. Count the occurrences of ‘a’ within the list

list=input("Enter names :")
count=0
for x in list:
    if x == 'a':
        count+=1
print("The occurrence of 'a' is :",count)
