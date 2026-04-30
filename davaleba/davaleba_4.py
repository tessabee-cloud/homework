#1

n = int(input('input a number: '))

while n >= 1:
    print(n)
    n -=1

#2

total = 0
while True:
    n = int(input('input a number or (0) to end: '))
    print(n)
    n +=n
    total += n

    if n == 0:

     print(total)
     break

#3

while True:
    n1 = 13
    guess = (int(input('input a number: ')))
    print(guess)

    if guess > n1:
        print('to high')

    elif guess < n1:
        print('too low')

    else:
        print('correct')
        break

#4

txt = input('write your text')

for c in txt:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        continue
    print(c, end=' ')
print()

#5
for i in range(0,9):
    print(i, end=' ')
print()
for i in range(5,15):
    print(i, end=' ')
print()
for i in range(0,20,2):
    print(i, end=' ')
print()
for i in range(10,1,-1):
    print(i, end=' ')
print()



