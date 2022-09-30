def great(a , b , c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c   

x = int(input("enter first number : "))   
y = int(input("enter second number : "))
z = int(input("enter third number : "))    
result =great(x,y,z)     
print("greatest number is :"+ str(result))
