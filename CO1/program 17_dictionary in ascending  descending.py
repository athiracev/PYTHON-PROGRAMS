#Sort dictionary in ascending and descending order

dict={"Athira":17,"Anu":2,"Linda":12,"Bonny":18,"Manjima":12,"Gokul":1,"Vishnu":18,"Navneeth":15,"Niranjan":5}
l1=list(dict.items())
l1.sort()
print("Dictionary in ascending order : ",l1)

l2=list(dict.items())
l2.sort(reverse=True)
print("Dictionary in descending order : ",l2)