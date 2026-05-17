from time import time


#1

def multiply(num1, num2):
    def check_nums(num1, num2):
        if num1 < 0 or num2 < 0:
            return 'actions can be done only with positive integers'
        else:
            return num1 * num2

    return check_nums(num1, num2)

print(multiply(2,-1))
print(multiply(3,4))
print(multiply(5,6))


#2

def formated_func(func):
    def wrapper(num1, num2):
        result = func(num1, num2)
        print(f'{'function called__'}{func.__name__}{', with attributes'} {num1} {'and'}  {num2}{', returned'} {result}')

    return wrapper

@formated_func
def add(num1, num2):
    return num1 + num2

add(3,4)

@formated_func
def subtract(num1, num2):
    return num1 - num2

subtract(7,4)



#3

import time


def repeat(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=5, delay=time.sleep(5))
def greeting(name):
    print( f'Hello, {name}!')


greeting('John')


#4

current_user_1 = {
    "username": "irakli",
    "role": "admin"
}
current_user_2 = {
    "username": "nikusha",
    "role": "manager"
}
current_user_3 = {
    "username": "tessa",
    "role": "developer"
}



def role_required(user_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') != user_role:
                print('permission denied!')
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@role_required('admin')
def delete_user(user_id):
    return  f'User with id {user_id} has been deleted.'


print(delete_user(current_user_1))


@role_required('admin')
def edit_user(user_id) :
    return f'User with id {user_id} has been updated.'

print(edit_user(current_user_2))


@role_required('admin')
def create_user(first_name):
    return f'User {first_name} has been created.'

print(create_user(current_user_3))
