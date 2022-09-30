def fun(n):
    if(n==0 or n==1):
       return 1
    else:
        return n+fun(n-1)

a= int(input("enter a number : "))    
print(fun(a))