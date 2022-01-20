# Create a string from given string where first and last characters exchanged.   [eg: python -> nythop]

str = input("Enter a string:")
print("Entered string:", str)
print("After exchange:")
print(str[-1] + str[1:-1] + str[0])