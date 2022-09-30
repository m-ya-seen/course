#lists are ordered , beginning with 0 

list= [1 , 2 , 3 ,4 ]
print(list)
print(list[1])
list[2]=99
print(list[2])

print(list[-2])
print(list[1:2])
print(list[2:])
list.sort()
print(list)

list.reverse()
print(list)

list.append(69)
print(list)

list.insert(1,0)
print(list)

list.pop(3)
print(list)

list.remove(69)
print(list)