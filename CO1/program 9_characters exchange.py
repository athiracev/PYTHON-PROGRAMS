# Create a string from given string where first and last characters exchanged.   [eg: python -> nythop]

str=input("Enter the string :")
print("Entered string :",str)
print("After exchange :",str[-1]+str[1:-1]+str[0])
