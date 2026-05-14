
#1

def sum_of_digits(n):
    leng = len(str(n))
    sum_nums = 0
    for i in range(leng+1):
        sum_nums +=i

    return sum_nums


print(sum_of_digits(123456))

#2

is_even = lambda n: n % 2 == 0

print(is_even(123456))

#3

students = [
    ("Luka", 15, 85),
    ("Ana", 14, 92),
    ("Giorgi", 16, 78),
    ("Nino", 15, 95)
]

sort_student= sorted(students, key=lambda x: (x[1], x[2]))
print(sort_student)


#4

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sort_words = sorted(words, key=lambda x: len(x), reverse = True)
print(sort_words)

#5

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

u_case_words= list(map(str.title, words))
print(u_case_words)

#6

numbers = [5, 12, 7, 18, 3, 24, 9]

filteted_numbers_1 = list(filter(lambda x: x >10, numbers))
filtered_numbers_2 = list(filter(lambda x: x % 3 == 0, filteted_numbers_1))

print(filtered_numbers_2)

