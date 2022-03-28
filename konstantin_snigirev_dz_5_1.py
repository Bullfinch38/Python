# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

print('Задание № 5.1\n')

def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = nums_generator(15)
for i in nums_gen:
    print(f'>>> next(odd_to_15)\n{i}')

print('\nЗадание № 5.2\n')

def num_generator(max_num):
    for num in range(1, max_num + 1, 2):
        print(f'>>> next(odd_to_15)\n{num}')


num_gen = num_generator(15)

print('\nЗадание № 5.1_v2\n')

def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num

nums_gen = nums_generator(15)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen)) # StopIteration

