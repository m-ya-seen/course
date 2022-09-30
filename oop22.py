from sys import settrace


class Employee:
    salary = 100000
    increment = 1.5

    @property
    def SalaryAfterIncrement(self):
        return self.salary * self.increment

    @SalaryAfterIncrement.setter 
    def SalaryAfterIncrement(self,salin):
        self.increment =salin/self.salary 

det = Employee()
print(det.SalaryAfterIncrement)
det.SalaryAfterIncrement(90000)