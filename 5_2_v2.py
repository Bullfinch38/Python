from itertools import zip_longest, islice


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Max', 'Bob']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
print('\nVariant 1\n')

my_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))

print(*islice(my_gen, len(tutors)), sep='\n')

print('\nVariant 2\n')
while len(klasses) <= len(tutors):
    klasses.append('None')
gen_2 = ((tutors[i], klasses[i]) for i in range(0, len(tutors)))
print(*gen_2, sep='\n')

print('\nVariant 3\n')
while len(klasses) <= len(tutors):
    klasses.append('None')
gen_3 = ((tutors, klasses) for tutors, klasses in zip(tutors, klasses))
print(*gen_3, sep='\n')