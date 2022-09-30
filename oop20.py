class Calci:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the square of {self.num} is {self.num **2}")

    def cube(self):
        print(f"the square of {self.num} is {self.num **3}")
       
            

a = Calci()
a.square()
a.cube()