import random

def rps(choicec , choicep):
    if choicec == choicep:
        return None
    elif choicec == 1:
        if choicep ==2:
            return True
        elif choicep ==3:
            return False

    elif choicec == 2 :
        if choicep ==3:
            return True
        elif choicep ==1:
            return False

    elif choicec == 3 :
        if choicep ==1:
            return True
        elif choicep ==2:
            return False        
           

print("computer's turn :")
choicec = random.randint(1,3)
print("your turn choose rock(1) , paper(2) , scissor(3")
choicep = int(input("enter an option :"))

a = rps(choicec , choicep)
if a == None:
    print("tie")
elif a ==False:
    print("you lose")
elif a ==True:
    print("you win")


