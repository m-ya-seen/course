#map and lamda
'''
list1 =[1,2,3,4,5]
square =list(map(lambda x:x*x , list1))
print(square)

'''

#typecasting using map
'''
num = ["1","2","3"]
num =list(map(int,num))
num[1] = num[1]+1
print (num[1])
'''
def square(a):
    return a**2
def cube(a):
    return a**3  

listo =[square, cube]
for i in range(10):
    res =list(map(lambda x :x(i) , listo))
    print(res)
