print("hello world")

a = ("12345")
a = int(a) #type casting
b= 5
print(a+b)

print(type(a)) #type checking

''' a = input("enter your name and age ")
a = str(a)
print(type(a)) '''

b = 1
c = 2
a>b

'''
a = input("enter integer a : ")
b = input("enter integer b : ")
a = int(a)
b = int(b)
print("average is",(a+b)/2)
print("square of a is " , a*a)
'''

#slicing 
c ="amongus"
d = c[5:7]
print(c[0:2] , c[2:5] , d ,c[-4:-1]) 

print(len(c))
print(c.count("u"))
print(c.endswith("us"))
print(c.capitalize())
print(c.find("lol"))
print(c.replace("among" , "s"))