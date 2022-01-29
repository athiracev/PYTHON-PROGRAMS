# Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.[eg: onion -> oni$n]

str=input("Enter the string :")
c=str[0]
str=str.replace(c,'$')
print(c+str[1:])
