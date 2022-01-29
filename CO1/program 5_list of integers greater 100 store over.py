# Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead

n = int(input("Enter the limit :"))
list = []
for x in range(n):
    x = int(input("Enter the number :"))
    if x < 100:
        list.append(x)
    else:
        list.append("over")
print(list)

