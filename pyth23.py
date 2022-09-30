def fizzBuzz(n):
    # Write your code here

    for i in range (n):
        i =1
        if (3%i == 0 and 5%i == 0):
            return print("FizzBuzz")
        elif(3%i == 0):
           return print("Fizz")
        elif(5%i == 0):
           return print("Buzz")
        elif(3%i !=0 and 5%i != 0):
           return print(f"{i}")      

n = int(input("enter"))

fizzBuzz(n)