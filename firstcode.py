#finding circle area
r=1.1
pi=3.14
area=pi*r*r
print("the area of the circle with radius1.1:",area)



#file extension
v= input("Enter Filename")
i = v.split(".")
if i[-1]=="py":
    print("Python")
if i[-1]=="java":
    print("Java")
else:
    print(i[-1])
