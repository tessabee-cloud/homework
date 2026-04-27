#1

num1 = input('your age')
num1 = int(num1)

if num1 <= 12:
    print('your a child')
elif num1 >= 13 and num1 <= 19:
    print('your a neetager')
elif num1 >= 20 and num1 <= 64:
    print('your an adult')
elif num1 >= 65:
    print('your a senior')


#2

score = input('score')
attendance = input('attendance')

if int(score) > 60 and int(attendance) > 75:
    print('passed')
else:
    print('failed')

#3
num1 = input('are you a student (yes/no)')
num2 = input('are you a member (yes/no)')

if num1 == 'yes' and  num2 == 'yes':
    print('you have additional discount')
elif num1 == 'no' or num2 == 'no':
    print('you have a discount')
if num1 == 'no' and num2 == 'no':
    print('you dont have a discount')

#4

user = input('your username')
if 3 < len(user) < 20 and user.isalnum():
    print('username correct')
else:
    print('username incorrect')

