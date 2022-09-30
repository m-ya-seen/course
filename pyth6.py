a = int(input("enter a number for its table "))
for i in range(1,11):
    # print (str(a) + "x" + str(i) + "=" + str(a*i))
    #fstring
    print(f"{a}x{i}={a*i}")
    i+1