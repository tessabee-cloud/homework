
 #1

cities = ['tbilisi','rustavi','gori','rustavi','kutaisi','gori','rustavi']

city_count1 = cities.count('tbilisi')

city_count2 = cities.count('rustavi')

city_count3 = cities.count('gori')

city_count4 = cities.count('kutaisi')

city_count_dict = {
     'tbilisi':city_count1,
     'rustavi':city_count2,
     'gori':city_count3,
     'kutaisi':city_count4,
 }


print(city_count_dict)


 #2

scores1 = {
     "math":   90,
     "english": 95,
     "history":     88
 }

print(scores1.items())

scores2 = {
     'math': 75,
     'french': 83,
     'art': 96,
     'english': 90
 }

print(scores2.items())

total_scores = {
     'math': (90,75),
     'english': (95,90),
     'history': 88,
     'art': 96,
     'french': 83
 }
print(total_scores)

 #3

person = {
     'name':'nika',
     'age': 23,
     'city': 'tbilisi'
 }

person_reverse = {v: k for k, v in person.items()}

print(person_reverse)

 #4

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

print(films1 & films2)
print(films1 - films2)
print(films2 - films1)
print(films1 | films2)

#5

info = {
    "კლასი 10A": {
        "გიორგი": {
            "ასაკი": 16,
            "საშუალო_ქულა": 8.7,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 8, "გამოცდა": False},
                "ისტორია": {"ქულა": 9, "გამოცდა": True},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 92,
            "დამატებითი": ["ფეხბურთი", "პროგრამირება"]
        },
        "ანა": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.4,
            "საგნები": {
                "მათემატიკა": {"ქულა": 10, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 9, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": False},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 98,
            "დამატებითი": ["ცეკვა"]
        },
        "დავით": {
            "ასაკი": 16,
            "საშუალო_ქულა": 7.2,
            "საგნები": {
                "მათემატიკა": {"ქულა": 6, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": True},
                "ინგლისური": {"ქულა": 9, "გამოცდა": False}
            },
            "დასწრება": 75,
            "დამატებითი": ["კალათბურთი", "პროგრამირება"]
        }
    },

    "კლასი 10B": {
        "მარიამ": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.1,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ბიოლოგია": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 95,
            "დამატებითი": ["მუსიკა", "ხატვა"]
        },
        "ლევან": {
            "ასაკი": 16,
            "საშუალო_ქულა": 6.8,
            "საგნები": {
                "მათემატიკა": {"ქულა": 5, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": False}
            },
            "დასწრება": 60,
            "დამატებითი": []
        }
    }
}

#1
names_a = info ["კლასი 10A"]
name_list_a=[]
for name in names_a:
    name_list_a.append(name)

print(name_list_a)

names_b = info ["კლასი 10B"]
name_list_b=[]
for name in names_b:
    name_list_b.append(name)

print(name_list_b)

giorgi = info ["კლასი 10A"] ["გიორგი"]
ana=info ["კლასი 10A"] ["ანა"]
daviti= info ["კლასი 10A"] ["დავით"]

mariam =info ["კლასი 10B"] ["მარიამ"]
levan = info ["კლასი 10B"] ["ლევან"]

print('გიორგი, საშუალო ქულა:', giorgi['საშუალო_ქულა'])
print('ანა, საშუალო ქულა:', ana['საშუალო_ქულა'])
print('დავით, საშუალო ქულა:', daviti['საშუალო_ქულა'])
print('მარიამ, საშუალო ქულა:', mariam['საშუალო_ქულა'])
print('ლევან, საშუალო ქულა:', levan['საშუალო_ქულა'])


# 2

avr_grade= {'გიორგი' :8.7,
    'ანა': 9.4,
    'დავით': 7.2,
    'მარიამ': 9.1,
    'ლევან' : 6.8,
}

rev= {v: k for k, v in avr_grade.items()}

avr_grade_list = (avr_grade.values())
print(max(avr_grade_list))
print(rev[9.4])

#3
attd= {'გიორგი' :92,
    'ანა': 98,
    'დავით': 75,
    'მარიამ': 95,
    'ლევან' : 60,
}

attd_rev = {v: k for k, v in attd.items()}

attendance = (giorgi["დასწრება"],ana["დასწრება"],daviti["დასწრება"],mariam["დასწრება"],levan["დასწრება"])
print(attendance)

attendance_90 = []
for a in attendance:
    if a > 90:
        attendance_90.append(a)

print(attendance_90)
print(attd_rev[92],attd_rev[98],attd_rev[95])

#4

stud_count_1 = len(names_a)
stud_count_2 = len(names_b)
print(stud_count_1 > stud_count_2)

#5

extras= (giorgi["დამატებითი"],ana["დამატებითი"],daviti["დამატებითი"],mariam["დამატებითი"],levan["დამატებითი"])
for i in extras:
    print(i)

it_studs= {
    'გიორგი' :('ფეხბურთი', 'პროგრამირება'),
    'ანა': 'ცეკვა',
    'დავით': ('კალათბურთი', 'პროგრამირება'),
    'მარიამ': ('მუსიკა', 'ხატვა'),
    'ლევან' :()
}

it_studs_list = ['გიორგი','დავით']

print(it_studs_list)

#6

avr_attd = 0
for i in attendance:
    avr_attd += i
avr_attd = avr_attd / len(attendance)
print(avr_attd)

#7

classes = {}

stud_list = []
for s in names_a:
    stud_list.append(s)
for s in names_b:
    stud_list.append(s)
print(stud_list)

classes[stud_list[0]] = len(giorgi["საგნები"])
classes[stud_list[1]] = len(ana["საგნები"])
classes[stud_list[2]] = len(daviti["საგნები"])
classes[stud_list[3]] = len(mariam["საგნები"])
classes[stud_list[4]] = len(levan["საგნები"])
print(classes)


#8

extr= {}

extr[stud_list[0]] = len(giorgi["დამატებითი"])
extr[stud_list[1]] = len(ana["დამატებითი"])
extr[stud_list[2]] = len(daviti["დამატებითი"])
extr[stud_list[3]] = len(mariam["დამატებითი"])
extr[stud_list[4]] = len(levan["დამატებითი"])

print(extr)

print('გიორგი')







