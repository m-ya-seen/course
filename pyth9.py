with open("filex.txt" , "r") as f:
    a=f.read()
    print(a)

if "shark" in a:
    print("shark is present ")
else:
    print("shark is not present")