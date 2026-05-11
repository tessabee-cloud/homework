
#1

def find_min_max(*args):
    return('max=', max(*args),'min=', min(*args))

print(find_min_max(1,2,3,4,5,6,7,8,9))


#2
def mult_nums(*args):

    total = 1

    for i in args:
        total *=i
    return total


print(mult_nums(1,2,3))

def sum_nums(*args):

    total = 0

    for i in args:
        total +=i
    return total

print(sum_nums(1,2,3,4))


def max_nums(*args):

    return max(args)

print(max_nums(1,2,3,4))

def min_nums(*args):
    return min(args)

print(min_nums(1,2,3,4))


def calculate(*args,operation):

    operations = operation.lower()
    if operations == 'sum':
        return sum_nums(*args)
    elif operations == 'min':
        return min_nums(*args)
    elif operations == 'max':
        return max_nums(*args)
    elif operations == 'mult':
        return mult_nums(*args)


print(calculate(1,2,3,4,5,6,7,8,9, operation="sum"))




#3

def format_user(first_name,last_name,**kwargs):
    return(f'{first_name} {last_name}{kwargs}')

print(format_user("John", "Doe", age=25, job="Developer"))


#4

def safe_divide(a, b):
    if b == 0:
        return("Cannot divide by zero")
    else:
        return(a/b , a % b)

print(safe_divide(32,3))
