# Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.


for i in range(1000,10000,1):

   for j in range(32,100,1):

       if i == j*j:

           string = str(i)

           if int(string[0])%2 == 0 and int(string[1])%2 == 0 and int(string[2])%2 == 0 and int(string[3])%2 == 0:

               print(i)

# method 2
# import math
#
# start = int(input("Enter a starting range in 4 digit:"))
# end = int(input("Enter an ending range in 4 digit:"))
# perfect = []
# for i in range(start,end+1):
#     flag = 0
#     num=i
#     while num>0 :
#         digit = num%10
#         if digit not in [0,2,4,6,8]:
#             flag=1
#             break
#         num=int(num/10)
#     if flag==0 and math.sqrt(i) % 1 == 0:
#         perfect.append(i)
# print("The list of perfect square numbers are:",perfect)

# method 3
# import math
# for i in range(1000,10000):
#     if math.sqrt(i)%1==0:
#         if int(i%10)%2==0:
#             if int((i/10)%10)%2==0:
#                 if int((i/100)%10)%2==0:
#                     if int((i/1000)%10)%2==0:
#                         print(i)
