class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def getData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")


class ItDepartment(Employee):
    min_salary = 30000

    def __init__(self, name, age, salary, department) -> None:
        self.department = department
        super().__init__(name, age, salary)

    def getDepartment(self):
        print(f"Department: {self.department}")

    @classmethod
    def min_it_salary(cls):
        return cls.min_salary

    @staticmethod
    def cal_salary(val):
        if val < 0:
            return "error"
        elif val < 30000:
            return "min salary"
        else:
            return "high salary"


# create Objeact
obj = ItDepartment("Nutthanon.Tho", 19, 45000, "IT")
obj.getData()
obj.getDepartment()
print("-----------------------------------------")

# use Static method
check_salary = ItDepartment.cal_salary(45000)
print("Status:", check_salary)
print("-----------------------------------------")


# use cls - classmethod
min_it_salary = ItDepartment.min_it_salary()
print("Start salary:", min_it_salary, "฿")
print("-----------------------------------------")
