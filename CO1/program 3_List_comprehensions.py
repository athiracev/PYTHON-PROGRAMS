# List comprehensions:
# (a) Generate positive list of numbers from a given list of integers

num=[10,0,-2,4,6,-7,8]
positive=[x for x in num if x > 0]
print(positive)

# (b) Square of N numbers

n=int(input("enter the limit:"))
square=[x*x for x in range(1,n+1)]
print(square)

# (c) Form a list of vowels selected from a given word

word="PredictableENGLISHMalayalam"
vowels="AaEeIiOoUu"
newlist=[x for x in word if x in vowels]
print(newlist)

# (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

word="english"
list=[ord(x) for x in word]
print(list)
