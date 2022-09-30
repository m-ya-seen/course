#set is a collection of non repetitive items 

a = { 1, 3 ,5 ,7 ,9 ,1}
print(type(a))
print(a)

b ={} #this is an empty dictionary
print(type(b))

#syntax for empty set
c=set()
print(type(c))

c.add(123)
print(c)
c.add(96)
print(c)

#tupple can be added in a set but not list,dictionary

c.add((1,2,3))
print(c)

#finding length of set
print(len(c))

c.remove(96)
print(c)

print(c.intersection({123, 2}))