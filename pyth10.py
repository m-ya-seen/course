dish={ "happy":"joyful",
        "sob" :"cry"
}
a=input("enter a word to find its meaning : ")

#print("it means :",dish[a])

print("it means :",dish.get(a)) #avoiding error
