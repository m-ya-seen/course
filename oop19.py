class Sob:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Details have been created")

    def getdetails(self):
        print(f"name is {self.name} , age is {self.age}")    


details=Sob("ace",20)       
details.getdetails() 



