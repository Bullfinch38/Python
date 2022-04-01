# Есть два списка:
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А') ('Анастасия', '7В')


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Bob', 'Max']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
print(type(tutors), type(klasses))

# for el in klasses:
#     tutors.append(el)
# print(tutors)

# for name in zip(tutors, klasses):
#     print(f'{type(name)}, {name}')

def get_name():
    for name in zip(tutors, klasses):
        yield name


a = get_name()
for i in a:
    print(type(i), i)
    if len(klasses) <= len(tutors):
        klasses.append('None')
