

#1

class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)


class Lecturer(Person):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)



student = Student("John", "Doe")
print(student.introduce())

lecturer = Lecturer("Jane", "Doe")
print(lecturer.introduce())


#2

class Profile:
    def __init__(self,password):
        self.__password = password

    def check_password(self,password):
        if password == self.__password:
            return True
        else:
            print('wrong password')
            return False

    def change_password(self,old_password,new_password):
        if old_password == self.__password:
            new_password = self.__password
            return True
        else:
            print('wrong password')
            return False


profile = Profile(input("Enter your password: "))

password = profile.check_password(input("Enter your password: "))

new_password = profile.change_password( input("Enter your old password: "), input('Enter your new password: '))

#3

class Product:
    def __init__(self,name,price):
        self.name = name
        self._price = price

    def set_price(self,price):
        if price < 0:
            raise ValueError('Price cannot be negative')
        else:
            self._price = price

    def get_price(self):
        return self._price


product = Product("apple",2)
print(product.get_price())
product.set_price(5)
print(product.get_price())


#4

class CreditCardPayment:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def pay(self,amount):
        if amount <= self.balance:
            print('your credit card payment went through')
            self.balance -= amount
            return True
        else:
            print('you dont have enough on your credit card balance')
            return False

class PayPalPayment:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def pay(self,amount):
        if amount <= self.balance:
            print('your PayPall payment went through')
            self.balance -= amount
            return True
        else:
            print('you dont have enough on your PayPall balance')
            return False

class CryptoPayment:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def pay(self,amount):
        if amount <= self.balance:
            print('your Crypto payment went through')
            self.balance -= amount
            return True
        else:
            print('you dont have enough on your Crypto balance')
            return False




pay = PayPalPayment(input("Enter your name: "),int(input("Enter your balance: ")))
pay = pay.pay(int(input("Enter your amount you want to pay: ")))


#5

class Cars:
    total_cars = 0
    def __init__(self, brand):
        self.brand = brand
        Cars.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


c1 = Cars("BMW")
c2 = Cars("Mercedes")
c3 = Cars("Toyota")

print(Cars.get_total_cars())



