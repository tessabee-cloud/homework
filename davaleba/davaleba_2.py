#1
num1 = input('your name')
num2 = input('your last name')
num1= num1.upper()
num2= num2.upper()

print(num1[0],',',num2[0])

#2
num1 = input('your word')
print(num1[::-1])

#3
num1 = input('your sentence')
num2 = input('word to change')
num3 = input('new word')

text = num1.replace(num2,num3)
print(text)

