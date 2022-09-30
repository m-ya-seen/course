class Library:
    def displaybook():
        print(dish)

    def lendbook():
        print("enter the book name you would like to lend :")

    def addbook():
        pass

    def returnbook():
        pass

dish ={"One piece":"Alex",
       "B" :"James",
       "C" :0,
       "D" :0          
}
while True:
    print('''***LIBRARY***
1)displaybooks
2)lendbooks  
3)addbooks
4)returnbooks
''')
    choice = int(input("select an operation to perform :"))
    if choice ==1 :
        Library.displaybook()
    elif choice ==2 :
        Library.lendbook()
    elif choice ==3 :
        Library.addbook()
    elif choice ==4 :
        Library.returnbook()            
    

