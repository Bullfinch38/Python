list_a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# # ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# # в "05" часов "17" минут температура воздуха была "+05" градусов
for i, s in enumerate(list_a):
    if s.isdigit():
        list_a[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        list_a[i] = f'{s[0]}{int(s[1:]):02d}"'
        print(' '.join(list_a))




# winter_months = ['декабрь', 'январь', 'февраль']
# print(isinstance(winter_months, list))
# winter_months.append(12) # only one number
# print(winter_months)
# winter_months.extend([1, 2]) # more than 1 number
# print(winter_months)
# # winter_months.append([1, 2]) # Двумерный массив
# print(winter_months)
#
# # print(winter_months.pop()) # вырезает последний объект из списка и возвращает как результат
# cut_winter_months = winter_months.pop() # можно вырезать любой элемент списка
# print(cut_winter_months)
#
# winter_months = ['декабрь', 'январь', 'январь', 'январь', 'февраль']
# while winter_months.count('январь') > 1:
#    winter_months.remove('январь')
#    print(winter_months)
# # ['декабрь', 'январь', 'январь', 'февраль']
# # ['декабрь', 'январь', 'февраль']
#
# winter_months = ['декабрь', 'январь', 'январь', 'январь', 'февраль']
# print(type(winter_months))
# print(type(list(winter_months)))
#
# a = 5
# print(id(a))