numbers = list(range(1, 1001))
print(numbers)

odd_numbers = list(range(1,1001,2))
print(odd_numbers)
print(len(odd_numbers)) # check

cubes = [value**3 for value in odd_numbers]

b = [] # создание нового списка
summ_1 = 0 # переменная, хранящая сумму чисел элемента списка cubes
for digits in cubes: # обход списка кубов нечетных чисел
    i = digits
    while digits != 0:
        summ_1 += digits % 10 # остаток от деления на 10 в summ_1
        digits = digits // 10
    if summ_1 % 7 == 0:
        b.append(i)
    summ_1 = 0
print(sum(b))

summ_digits_plus = 0
for digits in cubes:
    summ_2 = 0
    i = digits
    digits += 17
    while digits != 0:
        summ_2 += digits % 10
        digits = digits // 10
    if summ_2 % 7 == 0:
        summ_digits_plus += i + 17
print(summ_digits_plus)



# a = 1977
# s = 0
# while a > 0:
#     s += a % 10
#     a //= 10
# print(s)











