
#davaleba_8

#7

students= {
    "Luka":( 75, 85,67),
    "Ana":( 84, 92,87),
    "Giorgi":( 76, 77, 78),
}

# names=[]
# for student in students.keys():
#     names.append(student)
# print(names)
#
# scores_lst=[]
# for scores in students.values():
#     scores_lst.append(scores)
# print(scores_lst)


# def average(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum/len(args)
#
# print(average(1,2,3))
names_lst = []
scores_lst = []
for names,scores in students.items():
    names_lst.append(names)
    scores_lst.append(scores)

print(names_lst)
print(scores_lst)


# avr_score= map(lambda x: sum(x) / len(x), scores_lst)
# print(avr_score)

print(sum(scores_lst[0])/len(scores_lst[0]))