

#1

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f' {self.name} says: woof!')

    def info(self):
        print(self.name, self.age)

Dog_1 = Dog('Dobby',3)
Dog_1.bark()
Dog_1.info()


#2

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height)*2

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False


rectangle_1 = Rectangle(10,20)
print(rectangle_1.area())
print(rectangle_1.perimeter())
print(rectangle_1.is_square())



#3

class BankAccount:

    bank_name = 'step bank'

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):

        if (amount > self.balance):
            print('insufficient funds')
        else:
            self.balance -= amount

    def show_balance(self):
        print( BankAccount.bank_name, self.owner, self.balance)


account1 = BankAccount('liza',100)

account1.deposit(50)
account1.withdraw(200)
account1.show_balance()

#4

class Student:
    def __init__(self,name,grade):
        if grade < 0 or grade > 10:
            raise ValueError('Grade must be between 0 and 10')

        self.name = name
        self.grade = grade

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def average_grade(self):
        total = 0
        for student in self.students:
            total += student.grade
        return round(total/ len(self.students),2)

    def top_student(self):
        best = max(self.students,key=lambda student: student.grade)
        return best


student_1 = Student('liza',7)
student_2 = Student('tekla',10)

classroom_1 = Classroom()

classroom_1.add_student(student_1)
classroom_1.add_student(student_2)

print(classroom_1.average_grade())


