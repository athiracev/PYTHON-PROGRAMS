# Store a list of first names. Count the occurrences of ‘a’ within the list

list = []
c = 0
for i in range(3):
    x = input("Enter Names:")
    list.append(x)
for i in list:
    for j in i:
        if 'a' in j:
            c = c + 1
print("Number of a is:", c)