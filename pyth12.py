#conditional statements
#program to find greatest of four numbers 

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter fourth number : "))

if(a>b and a>c and a>d):
    print("greatest is ",a)
elif(b>a and b>c and b>d):
    print("greatest is ",b)
elif(c>b and c>a and c>d):
    print("greatest is ",c)
elif(d>b and d>c and d>a):
    print("greatest is ",d)            
