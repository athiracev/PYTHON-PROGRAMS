# Program to find the factorial of a number

fact = 1
num = int(input("Enter the number:"))
for i in range(1,num+1):
    fact = fact * i
print("Factorial of ",num,"is:", fact)

####  METHOD 2   #######

fact=1
i=1
n=int(input("Enter the number :"))
while i<=n:
    fact=fact*i
    i+=1
print("factorial is :",fact)
