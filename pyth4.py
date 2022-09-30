#finding greatest of three numbers

a =int(input("enter value of a :"))
b =int(input("enter value of b :"))
c =int(input("enter value of c :"))

if(a>b and a>c):
    print("greatest is :" ,a)
elif(b>a and b>c):
    print("greatest is :" ,b)
else:
    print("greatest is " ,c)    

